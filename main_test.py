import random

# from scene_cut import scene_cut_single
from moviepy.editor import VideoFileClip

if __name__ == '__main__':
    video = VideoFileClip('test/test.mp4')
    print(video.duration)
    random_time = random.randint(0, int(video.duration * 10))
    video.save_frame('test.jpg', t=random_time / 10)


