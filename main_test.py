import random
from paddleocr import PaddleOCR, draw_ocr
import cv2
from moviepy.editor import VideoFileClip



if __name__ == '__main__':
    video = VideoFileClip('test/美人如画_14.mp4')
    print(video.duration)
    for i in range(0, int(video.duration), 5):
        frame = video.get_frame(i)
        # 识别区域在底部1/6, 中央1/3
        frame = frame[int(frame.shape[0] * 5 / 6):, int(frame.shape[1] / 3):int(frame.shape[1] * 2 / 3)]
        # 灰度化、中值滤波去噪
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.medianBlur(frame, 3)
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        # 识别水平中文字幕
        res = ocr.ocr(frame, cls = True)

        if (res != [[]]):
            cv2.putText(frame, 'YES', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            cv2.putText(frame, 'NO', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        temp_str = 'temp/frame/temp' + str(i) + '.jpg'

        cv2.imwrite(temp_str, frame)
        # print(random.randint(0, 100))


