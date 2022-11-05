import multiprocessing
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QFileDialog

import ui.main as main
from ui.util import get_para
from detect.scene_cut import scene_cut_single
src_path = ''
target_path = ''

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)  # 定义一个发送str的信号，这里用的方法名与PyQt5不一样

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(10, loop.quit)
        loop.exec_()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = main.Ui_MainWidget()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化
        import sys
        sys.stdout = EmittingStr()
        self.ui.output_text.connect(sys.stdout, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten)
        sys.stderr = EmittingStr()
        self.ui.output_text.connect(sys.stderr, QtCore.SIGNAL("textWritten(QString)"), self.outputWritten)

    def select_src(self):
        global src_path
        src_path, _ = QFileDialog.getOpenFileName(
             self,  # 父窗口对象
             "选择需要检测的视频",  # 标题
             r"",  # 起始目录
             "视频类型 (*.mp4 *.avi *.mov)"  # 选择类型过滤项，过滤内容在括号中
         )
        # 修改label_src_path的文本
        self.ui.label_src_path.setText('选择视频路径:' + src_path)
        # 若src_path和target_path都不为空，则激活video_process按钮
        if src_path and target_path:
            self.ui.button_detect.setEnabled(True)


    def select_target(self):
        global target_path
        target_path = QFileDialog.getExistingDirectory(
            self,  # 父窗口对象
            "选择输出文件夹",  # 标题
            r""  # 起始目录
        )
        # 修改label_target_path的文本
        self.ui.label_target_path.setText('选择视频保存路径:' + target_path)
        # 若src_path和target_path都不为空，则激活video_process按钮
        if src_path and target_path:
            self.ui.button_detect.setEnabled(True)

    def video_process(self):
        video_scale, video_bitrate, audio_bitrate, audio_codec, preset, bitrate_encode = get_para(self.ui)
        start_time = self.ui.doubleSpinBox_start_time.value()
        end_time = self.ui.doubleSpinBox_end_time.value()
        video_fade_time = self.ui.doubleSpinBox_video_fade_time.value()
        audio_fade_time = self.ui.doubleSpinBox_audio_fade_time.value()
        scale_size = float(self.ui.doubleSpinBox_scale_size.value())/100
        if self.ui.radioButton_out_name.isChecked():
            out_format = 'name'
        elif self.ui.radioButton_out_num.isChecked():
            out_format = 'num'
        self.ui.progressBar.setValue(0)
        scene_cut_single(src_path=src_path, target_path=target_path,ui=self.ui, fadeout_time= video_fade_time
                         , audio_fadeout_time=audio_fade_time, bitrate=video_bitrate, audio_bitrate=audio_bitrate
                         , audio_codec=audio_codec, preset=preset, scale=video_scale, start_time=start_time, end_time=end_time,resize_value=scale_size
                         , out_format=out_format, bitrate_encode=bitrate_encode)

    def outputWritten(self, text):
        # self.edt_log.clear()
        cursor = self.ui.output_text.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.output_text.setTextCursor(cursor)
        self.ui.output_text.ensureCursorVisible()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())