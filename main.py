from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui.ui_vitool import Ui_Form
import cv2
import os

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 读入 UI 界面
        self.button_video.clicked.connect(self.readVideo)  # 读入视频路径
        self.button_output.clicked.connect(self.outputdir)  # 选择视频抽帧后的输出文件夹
        self.button_img.clicked.connect(self.readImg)  # 选择图片文件夹路径
        self.button_2img.clicked.connect(self.splitvideo)  # 点击后将视频抽帧为图片

    def readVideo(self):
        self.videopath = QFileDialog.getOpenFileName(self, '选择视频', '.', '视频文件(*.avi *.mp4 *.mkv)')[0]
        if self.videopath != '':
            self.lineEdit_videopath.setText(self.videopath)


    def outputdir(self):
        self.outputpath = QFileDialog.getExistingDirectory(self, '选择输出目录', '.')
        if self.outputpath != '':
            self.lineEdit_outputpath.setText(self.outputpath)

    def readImg(self):
        self.imgpath = QFileDialog.getExistingDirectory(self, '选择图片目录', '.')
        if self.imgpath != '':
            self.lineEdit_imgpath.setText(self.imgpath)

    def splitvideo(self):
        self.progressBar.reset()  # 进度条重置为0
        self.cap = cv2.VideoCapture(self.videopath)  # 打开视频文件
        if self.cap.isOpened():  # 如果视频已打开
            self.rate = self.cap.get(5)  # 视频帧率
            self.spinBox_frame.setMaximum(self.rate)  # 设置最大每rate帧抽一帧
            self.frames_num = self.cap.get(7)  # 获取视频总帧数CV_CAP_PROP_FRAME_COUNT
            self.videoname = self.videopath.split('/')[-1]  # 视频名称
            self.videoheight = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频高度
            self.videowidth = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频宽度
            frame = self.spinBox_frame.value()  # 每frame帧抽一帧
            self.img_num = int(self.frames_num / frame) - 1  # 拆分视频成图片数目为
            expand_name = '.jpg'  # 文件后缀名
            cnt = 0
            count = 0
            while 1:
                ret, frame2 = self.cap.read()
                cnt += 1
                if not ret:  # 视频读取完毕
                    break

                if cnt % frame == 0:
                    count += 1
                    try:
                        frame2 = cv2.resize(frame2, dsize=(int(self.videowidth/2), int(self.videoheight/2)),
                                            interpolation=cv2.INTER_AREA)  # 视频缩放
                    except:
                        print('此帧异常，也许为空')
                        continue

                    pic_path = os.path.join(self.outputpath, self.videoname + '_' + str(cnt).zfill(4) + expand_name)  # 文件名以0001这种四位编码标识帧数，所以如果帧数超过四位数，记得修改zfill(?)里的值
                    cv2.imwrite(pic_path, frame2, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
                    self.progressBar.setValue(int(count/self.img_num*100.0))
                    self.progresstext.setText("处理中({}/{})".format(count, self.img_num))
                    if count == self.img_num:
                        self.progresstext.setText("抽帧完成")
                        break
            self.cap.release()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
