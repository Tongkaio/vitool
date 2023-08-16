# 将视频裁剪成图片，按每10帧保存一张的方式
import cv2
import os
from cv2 import IMWRITE_JPEG_QUALITY

video_dir = 'F:\\video\\'  # 视频文件夹路径
ir_dir = 'F:\\frame_ir'  # ir图片保存路径
rgb_dir = 'F:\\frame_rgb'  # rgb图片保存路径


def get_video_duration(filename):  # 获取视频时长
    cap = cv2.VideoCapture(filename)  # 读取视频
    if cap.isOpened():  # 如果视频已打开
        rate = cap.get(5)  # 获取视频1s有多少帧
        frame_num = cap.get(7)  # 获取视频总帧数
        duration = frame_num / rate  # 时长 = 总帧数/1s的帧数
        return duration  # 返回时长
    return -1  # 打开视频失败


def process_video(i_video, o_pic, num, video_name, pic_num, size):  # 对视频按照frame的设置 保存成图片
    cap2 = cv2.VideoCapture(i_video)  # 打开视频文件
    expand_name = '.jpg'  # 文件后缀名
    if not cap2.isOpened():
        print("打开失败")

    cnt = 0
    count = 0
    while 1:
        ret, frame2 = cap2.read()
        cnt += 1
        if not ret:
            print('视频读取完毕')
            break

        if cnt % num == 0:
            count += 1
            try:
                frame2 = cv2.resize(frame2, size, interpolation=cv2.INTER_AREA)
            except:
                print('此帧异常，也许为空')
                continue

            pic_path = os.path.join(o_pic, video_name + '_' + str(cnt).zfill(4) + expand_name)  # 文件名以0001这种四位编码标识帧数，所以如果帧数超过四位数，记得修改zfill(?)里的值
            cv2.imwrite(pic_path, frame2, [int(IMWRITE_JPEG_QUALITY), 70])
            print(f"【已保存】{pic_path}")
            if count == pic_num:
                break


        # if count == 1:
        #     break


if __name__ == '__main__':
    for i in range(len(os.listdir(video_dir))):
        video_file = os.listdir(video_dir)[i]
        video_name = video_file.split('.')[0]  # 去掉后缀保留文件名
        video_path = os.path.join(video_dir, video_file)  # 视频文件路径
        cap = cv2.VideoCapture(video_path)  # 打开视频文件
        frames_num = cap.get(7)  # 获取视频总帧数CV_CAP_PROP_FRAME_COUNT
        frame = 1  # 每间隔frame帧抽1帧
        pic_num = int(frames_num / frame) - 1  # 拆分视频成图片数目为
        if (os.listdir(video_dir)[i][-5] == 'T'):
            print("IR视频")
            picture_dir = ir_dir
        else:
            print("找不到文件")
            picture_dir = '0'
            exit()
        picture_path = picture_dir
        if not os.path.exists(picture_dir):
            os.makedirs(picture_dir)
        if len(os.listdir(picture_path)) == 0:  # 文件夹空
            process_video(video_path, picture_path, frame, video_name, pic_num, (640, 512))
