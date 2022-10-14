from scene_cut import scene_cut_single
import os

if __name__ == '__main__':
    src_path = 'test/32集.mp4'
    target_path = 'cut_video'
    scene_cut_single(src_path, target_path)


