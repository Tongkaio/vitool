from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui.ui_vitool import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_video.clicked.connect(self.readVideo)
        self.button_output.clicked.connect(self.outputdir)

    def readVideo(self):
        self.videopath = QFileDialog.getOpenFileName(self, '选择视频', '.', '视频文件(*.avi *.mp4 *.mkv)')[0]
        self.lineEdit_videopath.setText(self.videopath)

    def outputdir(self):
        self.outputpath = QFileDialog.getExistingDirectory(self, '选择输出目录', '.')
        self.lineEdit_outputpath.setText(self.outputpath)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()