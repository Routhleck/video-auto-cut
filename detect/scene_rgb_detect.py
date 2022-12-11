from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize
from tqdm import tqdm

def scene_rgb_detect(src_path):
    # 读取视频
    video = VideoFileClip(src_path)

    video_resized = video.fx(resize, 0.15)
    diff = []
    # 将每一帧分别变为rgb三个通道，比对每两帧的rgb三个通道的差值，生成一个列表
    for i in tqdm(range(1, int(video_resized.duration) - 1)):
        frame_1 = video_resized.get_frame(i - 1)
        frame_2 = video_resized.get_frame(i)
        # 分别获取三个通道的值
        r1, g1, b1 = frame_1[:, :, 0], frame_1[:, :, 1], frame_1[:, :, 2]
        r2, g2, b2 = frame_2[:, :, 0], frame_2[:, :, 1], frame_2[:, :, 2]
        # 比对每两帧的rgb三个通道的差值，生成一个列表
        diff.append(abs(r1 - r2).sum() + abs(g1 - g2).sum() + abs(b1 - b2).sum())



    # 归一化diff
    for i in range(len(diff)):
        diff[i] = diff[i] / (video_resized.size[0] * video_resized.size[1])

    '''for i, diff_single in enumerate(diff):
        print(i, ':', diff_single)'''

    # 将diff中大于阈值的帧提取出来
    scene_list = []
    start = 0
    end = 0
    ifFirst = True
    for i in range(len(diff)):
        if diff[i] > 460:
            if ifFirst:
                end = i
                ifFirst = False
                scene_list.append([start, end])
                start = i + 1
            else:
                end = i
                scene_list.append([start, end])
                start = i + 1
        if i == len(diff) - 1:
            end = i
            scene_list.append([start, end])
        else:
            pass
    print(scene_list)
    return scene_list

