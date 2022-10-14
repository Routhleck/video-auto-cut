from spleeter.separator import Separator
from moviepy.editor import AudioFileClip
from sklearn.cluster import KMeans
import pydub
import numpy as np
import os
import time

def audio_adjust_to_scene_list(src_path, frame_per = 25, scene_list = []):
    audio_path = 'temp/audioFile/temp.wav'
    out_path = 'temp/audioFile'

    # 将视频转换为音频
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'视频转音频...')
    audio = AudioFileClip(src_path)
    # audio.write_audiofile(audio_path)

    k_num = int(audio.duration / 2)
    audio.close()
    
    # 分离音频
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频分离...')
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, out_path, duration = audio.duration)
    audio.close()
    os.remove(audio_path)

    # 语音片段的帧数
    audio_frame = []

    # 使用pydub读取分离出来的音频
    audio = pydub.AudioSegment.from_wav(out_path + '/temp/vocals.wav')

    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'音频分析...')
    '''print('audio_len: ', len(audio))
    print('audio frame rate: ',audio.frame_rate)
    print('audio duration seconds', audio.duration_seconds)'''
    # 使用pydub根据音频电平是否大于-32dB判断语音片段, 按视频的帧数进行迭代计算
    for i in range(0, len(audio), int(1000/ frame_per)):
        if audio[i:i + 1000/30].max_dBFS > -32:
            audio_frame.append(i / 1000 * frame_per)
    # os.remove(out_path + '/temp/vocals.wav')

    k_num = int(len(audio_frame) / (frame_per * 2))

    # print(audio_frame)

    # 将audio_frame转化为视频的帧
    audio_frame = np.array(audio_frame)

    x = audio_frame.reshape(-1, 1)

    # 将语音片段的帧数进行聚类
    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'语音片段聚类分析...')
    kmeans = KMeans(n_clusters=k_num, random_state=0).fit(x)

    # 获取聚类的每个类别的范围
    cluster_range = []
    for i in range(k_num):
        cluster_range.append([min(audio_frame[kmeans.labels_ == i]), max(audio_frame[kmeans.labels_ == i])])
    # print(cluster_range)

    # 将cluster_range 的每个第一个元素按照从小到大排序
    cluster_range = sorted(cluster_range, key=lambda x: x[0])

    print(time.strftime('%H:%M:%S', time.localtime(time.time())),'修正片段')
    # scene_i = 0
    # 遍历所有cluster_range, 修正scene_list
    for audio in cluster_range:
        while(scene_i < len(scene_list)):
            if audio[0] >= scene_list[i][0] and audio[1] > scene_list[i][1]:
                scene_list[i][1] = audio[1] + 5
                scene_list[i+1][0] = audio[1] + 6
                scene_i = i + 1
                break
            else:
                continue
    
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
    
    
