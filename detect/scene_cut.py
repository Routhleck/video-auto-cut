import random

from PySide6.QtWidgets import QApplication
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect.stats_manager import StatsManager
from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize
from moviepy.video.fx.fadeout import fadeout
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from detect.audio_process import audio_adjust_to_scene_list



import cv2
import os
import time
def frames_to_timecode(framerate,frames):
    """
    视频 通过视频帧转换成时间
    :param framerate: 视频帧率
    :param frames: 当前视频帧数
    :return:时间（00:00:01.01）
    """
    return '{0:02d}:{1:02d}:{2:02d}.{3:02d}'.format(int(frames / (3600 * framerate)),
                                                    int(frames / (60 * framerate) % 60),
                                                    int(frames / framerate % 60),
                                                    int(frames % framerate))

def get_scene_list(videopath, start_time, end_time, ui):
    # 定义re_scene_list 为视频切分场景的列表结果
    re_scene_list = []
    cap = cv2.VideoCapture(videopath)

    # 去掉开头结尾，开头时间设置为start_time，结尾时间设置为总时长 - end_time
    start_frame = int(start_time * cap.get(cv2.CAP_PROP_FPS))
    end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - int(end_time * cap.get(cv2.CAP_PROP_FPS))

    # 创建一个video_manager指向视频文件
    video_manager = VideoManager([videopath])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)

    # 添加ContentDetector算法(构造函数采用阈值等检测器选项)
    scene_manager.add_detector(ContentDetector())
    base_timecode = video_manager.get_base_timecode()

    try:
        frames_num = cap.get(7)
        # 设置缩减系数以提高处理速度
        video_manager.set_downscale_factor()

        # 启动video-manager
        video_manager.start()

        # 在video_manager上执行场景检测
        ui.progressBar.setValue(5)
        QApplication.processEvents()
        scene_manager.detect_scenes(frame_source=video_manager, show_progress=True)
        # 使用多线程更新进度条
        ui.progressBar.setValue(20)
        QApplication.processEvents()

        # 获取检测道德场景列表
        scene_list = scene_manager.get_scene_list(base_timecode)
        # 与FrameTimecodes一样，如果是，则可以对SceneList进行排序
        # 场景列表变为未排序

        print('List of scenes obtained:')

        # 若scene_list不为空,整理结果列表，否则，视频为单场景
        if scene_list:
            for i, scene in enumerate(scene_list):
                '''print('Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                    i + 1,
                    scene[0].get_timecode(), scene[0].get_frames(),
                    scene[1].get_timecode(), scene[1].get_frames(),))'''
                re_scene_list.append([scene[0].get_frames(), scene[1].get_frames()])
        else:
            re_scene_list.append([0, frames_num])

    finally:
        video_manager.release()

    ui.label_condition_name.setText('场景检测完成')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())), '场景检测完成')
    # 将re_scene_list中检查每个元素，如果元素的第一个值小于start_frame，第二个值大于end_frame，则将该元素删除
    remove_list = []
    for re_scene in re_scene_list:
        if re_scene[0] < start_frame or re_scene[1] > end_frame:
            remove_list.append(re_scene)
        else:
            pass

    # 将remove_list中的元素从re_scene_list中删除
    for i in remove_list:
        re_scene_list.remove(i)

    ui.progressBar.setValue(30)
    QApplication.processEvents()
    ui.label_condition_name.setText('检测修正')
    print(time.strftime('%H:%M:%S', time.localtime(time.time())), '检测修正...')
    # 若re_scene_list不为空,
    frame_per = cap.get(5)

    print(time.strftime('%H:%M:%S', time.localtime(time.time())), '场景检测完成')
    ui.progressBar.setValue(35)
    ui.label_condition_name.setText('场景检测完成')
    QApplication.processEvents()

    return re_scene_list, frame_per, start_frame, end_frame

# 将scene_list与audio_list合并优化
def optimize_scene_with_audio(scene_list, audio_list, frame_per):
    # 按audio_frame, 将scene_list合并
    min_len = 110 * frame_per
    max_len = 170 * frame_per

    first_flag = True
    new_scene_list = []
    new_scene = [0,0]
    for scene in scene_list:
        if new_scene[1] - new_scene[0] > min_len:
            for audio in audio_list:
                if new_scene[0] >= audio[0] and new_scene[1] < audio[1]:
                    pass
                elif new_scene[0] >= audio[1] or new_scene[1] < audio[0]:
                    pass
                elif new_scene[0] < audio[0] and new_scene[1] < audio[1]:
                    new_scene[1] = audio[1] + 1 * frame_per
                    new_scene_list.append(new_scene)
                    temp_scene = new_scene
                    new_scene = [temp_scene[1], temp_scene[1]]
                    break
                if audio == audio_list[-1]:
                    new_scene_list.append(new_scene)
                    temp_scene = new_scene
                    new_scene = [temp_scene[1], temp_scene[1]]
        elif scene == scene_list[-1]:
            new_scene[1] = scene[1]
            new_scene_list.append(new_scene)
        else:
            if first_flag:
                new_scene = scene
                first_flag = False
            else:
                if new_scene[1] > scene[1]:
                    pass
                else:
                    new_scene[1] = scene[1]

    print('新序列: ',new_scene_list)

    return new_scene_list


def build_scene(videopath, start_time, end_time, ui):
    re_scene_list, frame_per, start_frame, end_frame = get_scene_list(videopath, start_time, end_time, ui)
    if re_scene_list:
        
        # 将re_scene_list中的片段合并为符合min_len和max_len的片段
        for i in range(len(re_scene_list) - 1):
            if re_scene_list[i][1] - re_scene_list[i][0] < 10:
                re_scene_list[i + 1][0] = re_scene_list[i][0]
                re_scene_list[i] = []
        re_scene_list = [i for i in re_scene_list if i != []]

    # 人声检测
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'人声检测优化...')
    ui.label_condition_name.setText('人声检测优化')
    QApplication.processEvents()

    audio_list = audio_adjust_to_scene_list(videopath, frame_per,  start_frame=start_frame, end_frame=end_frame, ui=ui)

    final_list = optimize_scene_with_audio(re_scene_list, audio_list, frame_per)
    '''if final_list:
        # 视频帧数
        frame_per = cap.get(5)
        # 片段长度为60s到120s
        min_len = frame_per * 90
        max_len = frame_per * 150

        # 将final_list中的片段合并为符合min_len和max_len的片段
        for i in range(len(final_list) - 1):
            if final_list[i][1] - final_list[i][0] < min_len:
                final_list[i + 1][0] = final_list[i][0]
                final_list[i] = []
            elif final_list[i][1] - final_list[i][0] > max_len:
                final_list[i + 1][0] = final_list[i][0]
                final_list[i] = []
        final_list = [i for i in final_list if i != []]'''
    return frame_per, final_list



def scene_cut_single(src_path, 
                target_path,
                ui,
                fadeout_time = 1, 
                audio_fadeout_time = 1,
                bitrate = '4000k',
                codec = 'libx264',
                audio_codec = 'aac',
                audio_bitrate = '192k',
                preset = 'faster',
                scale = 'scale=1920:1080',
                aspect = '16:9',
                resize_value = 1.05,
                start_time = 0,
                end_time = 0
                ):
    """
    单视频切割
    :param src_path: 源视频路径
    :param target_path: 目标视频路径
    :param fadeout_time: 淡出时间
    :param audio_fadeout_time: 音频淡出时间
    :param bitrate: 视频码率
    :param codec: 视频编码
    :param fps: 视频帧率
    :param audio_codec: 音频编码
    :param audio_bitrate: 音频码率
    :param preset: 视频编码预设
    :param scale: 视频缩放
    :param aspect: 视频宽高比
    :param resize_value: 视频缩放比例
    """

    # 获取原视频名称
    src_name = src_path.split('/')[-1].split('.')[0]

    # 获取当前CPU的线程数
    cpu_num = os.cpu_count()

    # 获取切个场景帧数列表
    ui.label_condition_name.setText('开始检测场景')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'开始检测场景')
    frame_per, cut_frame = build_scene(src_path, start_time, end_time, ui)

    

    # cut frame转换为时间码00:00:00.00
    cut_time = []
    for i in cut_frame:
        cut_time.append([frames_to_timecode(frame_per, i[0]), frames_to_timecode(frame_per, i[1])])

    print(cut_time)

    ui.label_condition_name.setText('开始切割视频')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'开始切割视频')
    # 按cut_frame分别切割处理视频
    ui.progressBar.setValue(50)
    for i in range(len(cut_frame)):
        # 读取视频
        video = VideoFileClip(src_path)
        # 切割视频
        video = video.subclip(cut_time[i][0], cut_time[i][1])

        # 画面等比放大105%
        video = video.fx(resize, resize_value)

        # 结尾画面渐隐，声音渐隐
        video = video.fx(fadeout, fadeout_time)
        video = video.fx(audio_fadeout, audio_fadeout_time)

        # 视频比特率为4000kbps以上，使用CBR4.1编码，1080p，16:9
        video.write_videofile(target_path + '/' + src_name + '_' + str(i) + '.mp4', bitrate=bitrate, codec=codec, fps=frame_per, 
                            audio_codec=audio_codec, audio_bitrate=audio_bitrate,  threads=cpu_num, preset=preset,
                            ffmpeg_params=['-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p', '-vf', scale, '-aspect', aspect])
        # 随机截取一帧作为封面,保存为jpg
        random_time = random.randint(0, int(video.duration*10))
        video.save_frame(target_path + '/' + src_name + '_' + str(i) + '.jpg', t=random_time/10)
        ui.progressBar.setValue(50 + (i+1) * 50 / len(cut_frame))
        QApplication.processEvents()
    ui.progressBar.setValue(100)
    ui.label_condition_name.setText('视频处理完成')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'视频处理完成')
                            
