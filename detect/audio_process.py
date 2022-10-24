from PySide6.QtWidgets import QApplication
from spleeter.separator import Separator
from moviepy.editor import AudioFileClip, concatenate_audioclips
import pydub
import numpy as np
import os
import time

def audio_adjust_to_scene_list(src_path, frame_per = 25, scene_list = [], start_frame = 0, end_frame = 0, ui = None):
    
    # audio_path = 'temp/audioFile/temp.wav'
    audio_path = 'temp/audioFile/'
    out_path = 'temp/audioFile'
    # 一段语音识别阈值(s)
    threshold = 1.5

    # 将视频转换为音频
    ui.label_condition_name.setText('视频转音频')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'视频转音频...')
    
    # 按每段5分钟分割
    audio = AudioFileClip(src_path)
    # 获取音频时长
    audio_duration = audio.duration
    # 5分钟一段分割
    audio_segment = 5 * 60
    # 分割后的音频数量
    audio_segment_num = int(audio_duration / audio_segment)+1
    for i in range(audio_segment_num):
        print(i * audio_segment,'-' , (i + 1) * audio_segment)
        if i == audio_segment_num - 1:
            print(i * audio_segment,'-' , int(audio_duration))
            audio.subclip(i*audio_segment, int(audio_duration)).write_audiofile(audio_path+str(i)+'.wav')
        else:
            audio.subclip(i * audio_segment, (i + 1) * audio_segment).write_audiofile(audio_path + str(i) + '.wav')
    # audio.write_audiofile(audio_path)

    
    ui.progressBar.setValue(40)
    QApplication.processEvents()

    audio.close()
    
    # 分离音频
    ui.label_condition_name.setText('音频分离')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频分离...')
    # separator禁用GPU
    separator = Separator('spleeter:2stems')
    for i in range(audio_segment_num):
        separator.separate_to_file(audio_path + str(i) + '.wav', out_path + '/' + str(i), synchronous = True)
        print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频片段', str(i),'分离完成')
    # for i in range(audio_segment_num):
        # os.remove(audio_path + str(i) + '.wav')
    ui.progressBar.setValue(45)
    QApplication.processEvents()

    # 合并音频
    ui.label_condition_name.setText('音频合并')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频合并...')
    # 将分离的音频合并
    audio_list = []
    for i in range(audio_segment_num):
        audio_list.append(AudioFileClip(out_path + '/' + str(i)+ '/' +str(i) + '/vocals.wav'))

    audio = concatenate_audioclips(audio_list)
    audio.write_audiofile(out_path + '/vocals.wav')
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频合并完成')

    # 语音片段的帧数
    audio_frame = []

    # 使用pydub读取分离出来的音频
    audio = pydub.AudioSegment.from_wav(out_path + '/vocals.wav')

    ui.progressBar.setValue(47)
    ui.label_condition_name.setText('音频分析')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频分析...')
    '''print('audio_len: ', len(audio))
    print('audio frame rate: ',audio.frame_rate)
    print('audio duration seconds', audio.duration_seconds)'''

    left = 0
    right = 0
    isStart = True
    frame_count = 0

    # 使用pydub根据音频电平是否大于-32dB判断语音片段, 按视频的帧数进行迭代计算
    for i in range(0, len(audio), int(1000/ frame_per)):
        if audio[i:i + 1000/30].max_dBFS > -32:
            if isStart == True:
                frame_count = 0
                left = i / 1000 * frame_per
                right = i / 1000 * frame_per
                isStart = False
            else:
                right = i / 1000 * frame_per
                frame_count = 0
        else:
            if isStart == False:
                frame_count += 1
                if (frame_count > threshold * frame_per):
                    audio_frame.append([left, right])
                    frame_count = 0
                    isStart = True
            else:
                continue
    # os.remove(out_path + '/temp/vocals.wav')

    # 将re_scene_list中检查每个元素，如果元素的第一个值小于start_frame，第二个值大于end_frame，则将该元素删除
    remove_list = []
    for re_scene in audio_frame:
        if re_scene[0] < start_frame or re_scene[1] > end_frame:
            remove_list.append(re_scene)
        else:
            pass
    
    # 将remove_list中的元素从re_scene_list中删除
    for i in remove_list:
        audio_frame.remove(i)

    ui.progressBar.setValue(49)
    ui.label_condition_name.setText('修正片段')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'修正片段')

    # 将audio_frame换算成秒
    audio_frame_second = []
    for i in audio_frame:
        audio_frame_second.append([i[0]/frame_per, i[1]/frame_per])
    print(audio_frame_second)

    # 遍历所有audio_frame, 修正scene_list
    last_fix = 0
    for audio in audio_frame:
        for i in range(last_fix, len(scene_list)):
            if audio[0] >= scene_list[i][0] and audio[1] > scene_list[i][1]:
                scene_list[i][1] = audio[1]
                if i + 1 < len(scene_list):
                    scene_list[i+1][0] = audio[1] + 1
                last_fix = i + 1
                break

    ui.progressBar.setValue(50)
    ui.label_condition_name.setText('音频优化完成')
    QApplication.processEvents()
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频优化完成')
    return scene_list
    '''# 将src_path中的音频按10分钟一段提取出来
    audio = AudioFileClip(src_path)
    audio_duration = audio.duration
    audio.close()
    audio_segment = 600
    audio_segment_num = int(audio_duration / audio_segment)
    audio_segment_list = []
    for i in range(audio_segment_num):
        audio_segment_list.append([i * audio_segment, (i + 1) * audio_segment])
    audio_segment_list.append([audio_segment_num * audio_segment, audio_duration])
    print(audio_segment_list)

    # 解决unable to allocate array with shape and data type
    audio_adapter = AudioAdapter.default()

    # 将src_path中的音频按10分钟一段提取出来
    for num, i in enumerate(audio_segment_list):
        audio = AudioFileClip(src_path).subclip(i[0], i[1])
        audio.write_audiofile(out_path + '/temp' + str(num) + '.wav')
        audio.close()
        # 分离音频
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(out_path + '/temp' + str(num) + '.wav', out_path + '/' + str(num),audio_adapter=audio_adapter)
        # 删除临时文件
        os.remove(out_path + '/temp' + str(num) + '.wav')
    
    # 将分离出来的音频合并
    audio_list = []
    for i in range(audio_segment_num + 1):
        audio_list.append(AudioFileClip(out_path + '/' + str(i) + 'temp' + str(i) + '/vocals.wav'))
    
    print(audio_list)
    
    # 合并audio_list中的音频
    final_audio = audio_list[0]
    for i in range(1, len(audio_list)):
        final_audio = final_audio.append(audio_list[i])
    final_audio.write_audiofile(audio_path)
    final_audio.close()'''
    
    
