from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize as fx_resize
from moviepy.video.fx.crop import crop
from scene_cut import save_cover

clip = VideoFileClip("F:/BaiduNetdiskDownload/cut_video/美人如画_高清SDR_美人如画_14.mp4")

clip = clip.fx(fx_resize, (1920, 1080))

clip = clip.fx(fx_resize, 1.15)

# 截图
save_cover(False, clip, "F:/BaiduNetdiskDownload/cut_video", 0)