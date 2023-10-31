from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui.ui_vitool import Ui_Form
import cv2
import os


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 读入 UI 界面
        self.bind()  # 绑定信号与槽

    def bind(self):
        self.button_video.clicked.connect(self.readVideo)  # 读入视频路径
        self.button_output.clicked.connect(self.outputdir_1)  # 选择视频抽帧后的输出文件夹
        self.button_img.clicked.connect(self.readImg)  # 选择图片文件夹路径
        self.button_output_2.clicked.connect(self.outputdir_2)  # 选择视频抽帧后的输出文件夹
        self.button_2img.clicked.connect(self.video2img)  # 点击后将视频抽帧为图片
        self.button_2video.clicked.connect(self.img2video)  # 点击后将图片合并为视频
        self.spinBox_frame.valueChanged.connect(self.setfps)  # 设置帧率
        self.checkBox_deleteimg.stateChanged.connect(self.setenabled)  # 是否允许删除图片

    def setenabled(self):
        if not self.checkBox_deleteimg.isChecked():  # 如果不允许删除图片
            self.checkBox_deletedir.setChecked(False)  # 取消勾选“删除文件夹”
            self.checkBox_deletedir.setEnabled(False)  # 禁止删除文件夹
        else:
            self.checkBox_deletedir.setEnabled(True)  # 允许删除文件夹

    def setfps(self):
        self.spinBox_fps.setValue(int(self.rate/self.spinBox_frame.value()))  # 设置合并视频后的帧率

    def readVideo(self):
        self.videopath = QFileDialog.getOpenFileName(self, '选择视频', '.', '视频文件(*.avi *.mp4 *.mkv)')[0]
        if self.videopath != '':
            self.lineEdit_videopath.setText(self.videopath)
        self.cap = cv2.VideoCapture(self.videopath)  # 打开视频文件
        if self.cap.isOpened():  # 如果视频已打开
            self.rate = self.cap.get(5)  # 视频帧率
            self.spinBox_frame.setMaximum(self.rate)  # 设置最大每rate帧抽一帧
            self.frames_num = self.cap.get(7)  # 获取视频总帧数CV_CAP_PROP_FRAME_COUNT
            self.videoname = self.videopath.split('/')[-1]  # 视频名称
            self.videoheight = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频高度
            self.videowidth = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频宽度
            self.spinBox_fps.setValue(int(self.rate/self.spinBox_frame.value()))  # 设置合并视频后的帧率
            self.cap.release()

    def outputdir_1(self):
        self.outputpath_1 = QFileDialog.getExistingDirectory(self, '选择输出目录', '.')
        if self.outputpath_1 != '':
            self.lineEdit_outputpath.setText(self.outputpath_1)
            self.lineEdit_imgpath.setText(self.outputpath_1)
            self.imgpath = self.outputpath_1

    def readImg(self):
        self.imgpath = QFileDialog.getExistingDirectory(self, '选择图片目录', '.')
        if self.imgpath != '':
            self.lineEdit_imgpath.setText(self.imgpath)

    def outputdir_2(self):
        self.outputpath_2 = QFileDialog.getExistingDirectory(self, '选择输出目录', '.')
        if self.outputpath_2 != '':
            self.lineEdit_outputpath_2.setText(self.outputpath_2)

    def video2img(self):
        self.progressBar.reset()  # 进度条重置为0
        self.cap = cv2.VideoCapture(self.videopath)  # 打开视频文件
        suffixLength = max(self.spinBox_SuffixLength.value(), len(str(self.frames_num)))  # 后缀位数取决于用户设置的值和frames_num中较大的那个
        if self.cap.isOpened():  # 如果视频已打开
            frame = self.spinBox_frame.value()
            img_num = int(self.frames_num / frame) - 1  # 拆分视频成图片数目为
            expand_name = '.jpg'  # 文件后缀名
            cnt = 0  # 记录已经读取多少帧了
            count = 0  # 记录已经抽取多少张图片了
            while 1:
                ret, frame2 = self.cap.read()
                cnt += 1
                if not ret:  # 视频读取完毕
                    break

                if cnt % frame == 0:
                    count += 1
                    # try:  # 缩减画面尺寸
                    #     frame2 = cv2.resize(frame2, dsize=(640, 512),
                    #                         interpolation=cv2.INTER_AREA)
                    # except:
                    #     print('此帧异常，也许为空')
                    #     continue

                    # 图片的后缀是_0001.jpg这种形式其中0001的位数由suffixLength，即视频有多少帧
                    # 如果视频有123张图片，那么后缀长度就是3

                    pic_path = ''
                    if (self.lineEdit_ImgPrefix.text()):
                        pic_path = os.path.join(self.outputpath_1, self.lineEdit_ImgPrefix.text()
                                                + '_' + str(cnt).zfill(suffixLength) + expand_name)
                    else:
                        pic_path = os.path.join(self.outputpath_1, self.videoname
                                                + '_' + str(cnt).zfill(suffixLength) + expand_name)
                    cv2.imwrite(pic_path, frame2, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
                    # 显示进度条
                    self.progressBar.setValue(int(count/img_num*100.0))
                    self.progresstext.setText("处理中({}/{})".format(count, img_num))
                    # 完成抽帧
                    if count == img_num:
                        self.progresstext.setText("抽帧完成")
                        break
            self.cap.release()

    def img2video(self):
        self.progressBar.reset()  # 进度条重置为0
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        output_name = self.imgpath.split('/')[-1] + '.avi'
        writer = cv2.VideoWriter(os.path.join(self.outputpath_2, output_name), fourcc,
                                 self.spinBox_fps.value(), (960, 540), True)
        imglist = os.listdir(self.imgpath)
        imglist.sort()
        count = 0
        img_num = len(imglist)
        for img in imglist:
            filename = os.path.join(self.imgpath, img)
            img = cv2.imread(filename)
            if img is None:
                print(filename + " is error!")
                continue
            count += 1
            # 显示进度条
            self.progressBar.setValue(int(count / img_num * 100.0))
            self.progresstext.setText("处理中({}/{})".format(count, img_num))
            writer.write(img)
            if self.checkBox_deleteimg.isChecked():
                os.remove(filename)
        if self.checkBox_deletedir.isChecked():
            try:
                os.rmdir(self.imgpath)
            except:
                print("目录删除失败")
        self.progresstext.setText("合并完成")
        writer.release()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
