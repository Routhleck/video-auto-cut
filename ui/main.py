# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1080, 778)
        self.widget_control = QWidget(MainWidget)
        self.widget_control.setObjectName(u"widget_control")
        self.widget_control.setGeometry(QRect(10, 20, 211, 201))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(18)
        self.widget_control.setFont(font)
        self.widget_control.setMouseTracking(False)
        self.widget_control.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.4)")
        self.verticalLayout = QVBoxLayout(self.widget_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_select_src = QPushButton(self.widget_control)
        self.button_select_src.setObjectName(u"button_select_src")
        self.button_select_src.setFont(font)

        self.verticalLayout.addWidget(self.button_select_src)

        self.button_select_target = QPushButton(self.widget_control)
        self.button_select_target.setObjectName(u"button_select_target")
        self.button_select_target.setFont(font)

        self.verticalLayout.addWidget(self.button_select_target)

        self.button_detect = QPushButton(self.widget_control)
        self.button_detect.setObjectName(u"button_detect")
        self.button_detect.setEnabled(False)
        self.button_detect.setFont(font)

        self.verticalLayout.addWidget(self.button_detect)

        self.widget_config = QWidget(MainWidget)
        self.widget_config.setObjectName(u"widget_config")
        self.widget_config.setGeometry(QRect(220, 20, 851, 301))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(14)
        self.widget_config.setFont(font1)
        self.widget_config.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.4)")
        self.gridLayout = QGridLayout(self.widget_config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_mode = QLabel(self.widget_config)
        self.label_mode.setObjectName(u"label_mode")

        self.gridLayout.addWidget(self.label_mode, 2, 0, 1, 1)

        self.comboBox_mode = QComboBox(self.widget_config)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")

        self.gridLayout.addWidget(self.comboBox_mode, 2, 1, 1, 1)

        self.comboBox_bitrate = QComboBox(self.widget_config)
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.addItem("")
        self.comboBox_bitrate.setObjectName(u"comboBox_bitrate")

        self.gridLayout.addWidget(self.comboBox_bitrate, 4, 1, 1, 1)

        self.label_bitrate = QLabel(self.widget_config)
        self.label_bitrate.setObjectName(u"label_bitrate")

        self.gridLayout.addWidget(self.label_bitrate, 4, 0, 1, 1)

        self.label_scale = QLabel(self.widget_config)
        self.label_scale.setObjectName(u"label_scale")

        self.gridLayout.addWidget(self.label_scale, 3, 0, 1, 1)

        self.label_config = QLabel(self.widget_config)
        self.label_config.setObjectName(u"label_config")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(36)
        self.label_config.setFont(font2)
        self.label_config.setStyleSheet(u"")
        self.label_config.setTextFormat(Qt.AutoText)
        self.label_config.setScaledContents(False)
        self.label_config.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_config, 0, 0, 1, 4)

        self.comboBox_scale = QComboBox(self.widget_config)
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.setObjectName(u"comboBox_scale")

        self.gridLayout.addWidget(self.comboBox_scale, 3, 1, 1, 1)

        self.label_src_path = QLabel(self.widget_config)
        self.label_src_path.setObjectName(u"label_src_path")
        self.label_src_path.setWordWrap(True)

        self.gridLayout.addWidget(self.label_src_path, 1, 0, 1, 2)

        self.label_target_path = QLabel(self.widget_config)
        self.label_target_path.setObjectName(u"label_target_path")
        self.label_target_path.setWordWrap(True)

        self.gridLayout.addWidget(self.label_target_path, 1, 2, 1, 2)

        self.label_audio_bitrate = QLabel(self.widget_config)
        self.label_audio_bitrate.setObjectName(u"label_audio_bitrate")

        self.gridLayout.addWidget(self.label_audio_bitrate, 2, 2, 1, 1)

        self.comboBox_audio_bitrate = QComboBox(self.widget_config)
        self.comboBox_audio_bitrate.addItem("")
        self.comboBox_audio_bitrate.addItem("")
        self.comboBox_audio_bitrate.addItem("")
        self.comboBox_audio_bitrate.addItem("")
        self.comboBox_audio_bitrate.setObjectName(u"comboBox_audio_bitrate")

        self.gridLayout.addWidget(self.comboBox_audio_bitrate, 2, 3, 1, 1)

        self.label_audio_codec = QLabel(self.widget_config)
        self.label_audio_codec.setObjectName(u"label_audio_codec")

        self.gridLayout.addWidget(self.label_audio_codec, 3, 2, 1, 1)

        self.comboBox_audio_codec = QComboBox(self.widget_config)
        self.comboBox_audio_codec.addItem("")
        self.comboBox_audio_codec.addItem("")
        self.comboBox_audio_codec.addItem("")
        self.comboBox_audio_codec.setObjectName(u"comboBox_audio_codec")

        self.gridLayout.addWidget(self.comboBox_audio_codec, 3, 3, 1, 1)

        self.label_preset = QLabel(self.widget_config)
        self.label_preset.setObjectName(u"label_preset")

        self.gridLayout.addWidget(self.label_preset, 4, 2, 1, 1)

        self.comboBox_preset = QComboBox(self.widget_config)
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.addItem("")
        self.comboBox_preset.setObjectName(u"comboBox_preset")

        self.gridLayout.addWidget(self.comboBox_preset, 4, 3, 1, 1)

        self.widget_effect_config = QWidget(MainWidget)
        self.widget_effect_config.setObjectName(u"widget_effect_config")
        self.widget_effect_config.setGeometry(QRect(220, 320, 851, 241))
        self.widget_effect_config.setFont(font1)
        self.widget_effect_config.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.4)")
        self.gridLayout_2 = QGridLayout(self.widget_effect_config)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_video_fade_time = QLabel(self.widget_effect_config)
        self.label_video_fade_time.setObjectName(u"label_video_fade_time")
        self.label_video_fade_time.setFont(font1)

        self.gridLayout_2.addWidget(self.label_video_fade_time, 2, 0, 1, 1)

        self.label_audio_fade_time = QLabel(self.widget_effect_config)
        self.label_audio_fade_time.setObjectName(u"label_audio_fade_time")
        self.label_audio_fade_time.setFont(font1)
        self.label_audio_fade_time.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.label_audio_fade_time, 2, 2, 1, 1)

        self.label_start_time = QLabel(self.widget_effect_config)
        self.label_start_time.setObjectName(u"label_start_time")
        self.label_start_time.setFont(font1)

        self.gridLayout_2.addWidget(self.label_start_time, 1, 0, 1, 1)

        self.label_effect_config = QLabel(self.widget_effect_config)
        self.label_effect_config.setObjectName(u"label_effect_config")
        self.label_effect_config.setFont(font2)
        self.label_effect_config.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_effect_config, 0, 0, 1, 4)

        self.doubleSpinBox_start_time = QDoubleSpinBox(self.widget_effect_config)
        self.doubleSpinBox_start_time.setObjectName(u"doubleSpinBox_start_time")
        self.doubleSpinBox_start_time.setFont(font1)
        self.doubleSpinBox_start_time.setDecimals(1)
        self.doubleSpinBox_start_time.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_start_time, 1, 1, 1, 1)

        self.label_end_time = QLabel(self.widget_effect_config)
        self.label_end_time.setObjectName(u"label_end_time")
        self.label_end_time.setFont(font1)

        self.gridLayout_2.addWidget(self.label_end_time, 1, 2, 1, 1)

        self.doubleSpinBox_end_time = QDoubleSpinBox(self.widget_effect_config)
        self.doubleSpinBox_end_time.setObjectName(u"doubleSpinBox_end_time")
        self.doubleSpinBox_end_time.setFont(font1)
        self.doubleSpinBox_end_time.setDecimals(1)
        self.doubleSpinBox_end_time.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_end_time, 1, 3, 1, 1)

        self.doubleSpinBox_video_fade_time = QDoubleSpinBox(self.widget_effect_config)
        self.doubleSpinBox_video_fade_time.setObjectName(u"doubleSpinBox_video_fade_time")
        self.doubleSpinBox_video_fade_time.setFont(font1)
        self.doubleSpinBox_video_fade_time.setDecimals(1)
        self.doubleSpinBox_video_fade_time.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_video_fade_time, 2, 1, 1, 1)

        self.doubleSpinBox_audio_fade_time = QDoubleSpinBox(self.widget_effect_config)
        self.doubleSpinBox_audio_fade_time.setObjectName(u"doubleSpinBox_audio_fade_time")
        self.doubleSpinBox_audio_fade_time.setFont(font1)
        self.doubleSpinBox_audio_fade_time.setDecimals(1)
        self.doubleSpinBox_audio_fade_time.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_audio_fade_time, 2, 3, 1, 1)

        self.label_scale_size = QLabel(self.widget_effect_config)
        self.label_scale_size.setObjectName(u"label_scale_size")
        self.label_scale_size.setFont(font1)

        self.gridLayout_2.addWidget(self.label_scale_size, 3, 0, 1, 1)

        self.doubleSpinBox_scale_size = QDoubleSpinBox(self.widget_effect_config)
        self.doubleSpinBox_scale_size.setObjectName(u"doubleSpinBox_scale_size")
        self.doubleSpinBox_scale_size.setFont(font1)
        self.doubleSpinBox_scale_size.setDecimals(0)
        self.doubleSpinBox_scale_size.setMaximum(500.000000000000000)
        self.doubleSpinBox_scale_size.setValue(105.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_scale_size, 3, 1, 1, 1)

        self.widget_process = QWidget(MainWidget)
        self.widget_process.setObjectName(u"widget_process")
        self.widget_process.setGeometry(QRect(10, 570, 1061, 201))
        self.widget_process.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.4)")
        self.gridLayout_3 = QGridLayout(self.widget_process)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.progressBar = QProgressBar(self.widget_process)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 0, 0, 1, 1)

        self.output_text = QTextEdit(self.widget_process)
        self.output_text.setObjectName(u"output_text")

        self.gridLayout_3.addWidget(self.output_text, 1, 0, 1, 1)

        self.widget_condition = QWidget(MainWidget)
        self.widget_condition.setObjectName(u"widget_condition")
        self.widget_condition.setGeometry(QRect(10, 220, 211, 341))
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(20)
        self.widget_condition.setFont(font3)
        self.widget_condition.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.4)")
        self.gridLayout_4 = QGridLayout(self.widget_condition)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_condition = QLabel(self.widget_condition)
        self.label_condition.setObjectName(u"label_condition")
        self.label_condition.setFont(font)
        self.label_condition.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_condition, 0, 0, 1, 1)

        self.label_condition_name = QLabel(self.widget_condition)
        self.label_condition_name.setObjectName(u"label_condition_name")
        self.label_condition_name.setFont(font)
        self.label_condition_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_condition_name, 1, 0, 1, 1)


        self.retranslateUi(MainWidget)
        self.button_select_src.clicked.connect(MainWidget.select_src)
        self.button_select_target.clicked.connect(MainWidget.select_target)
        self.button_detect.clicked.connect(MainWidget.video_process)

        self.comboBox_bitrate.setCurrentIndex(3)
        self.comboBox_scale.setCurrentIndex(0)
        self.comboBox_audio_bitrate.setCurrentIndex(1)
        self.comboBox_preset.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u573a\u666f\u68c0\u6d4b_demo", None))
        self.button_select_src.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9\u68c0\u6d4b\u89c6\u9891", None))
        self.button_select_target.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.button_detect.setText(QCoreApplication.translate("MainWidget", u"\u68c0\u6d4b\u5e76\u5bfc\u51fa\u89c6\u9891", None))
        self.label_mode.setText(QCoreApplication.translate("MainWidget", u"\u8f93\u51fa\u9884\u5b9a\u6a21\u5f0f", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("MainWidget", u"1080p\u9ed8\u8ba4", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("MainWidget", u"720p\u9ed8\u8ba4", None))

        self.comboBox_bitrate.setItemText(0, QCoreApplication.translate("MainWidget", u"1000kbps", None))
        self.comboBox_bitrate.setItemText(1, QCoreApplication.translate("MainWidget", u"2000kbps", None))
        self.comboBox_bitrate.setItemText(2, QCoreApplication.translate("MainWidget", u"3000kbps", None))
        self.comboBox_bitrate.setItemText(3, QCoreApplication.translate("MainWidget", u"4000kbps", None))
        self.comboBox_bitrate.setItemText(4, QCoreApplication.translate("MainWidget", u"5000kbps", None))
        self.comboBox_bitrate.setItemText(5, QCoreApplication.translate("MainWidget", u"6000kbps", None))
        self.comboBox_bitrate.setItemText(6, QCoreApplication.translate("MainWidget", u"7000kbps", None))
        self.comboBox_bitrate.setItemText(7, QCoreApplication.translate("MainWidget", u"8000kbps", None))
        self.comboBox_bitrate.setItemText(8, QCoreApplication.translate("MainWidget", u"9000kbps", None))
        self.comboBox_bitrate.setItemText(9, QCoreApplication.translate("MainWidget", u"10000kbps", None))

        self.comboBox_bitrate.setCurrentText(QCoreApplication.translate("MainWidget", u"4000kbps", None))
        self.label_bitrate.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u6bd4\u7279\u7387", None))
        self.label_scale.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u5c3a\u5bf8", None))
        self.label_config.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u53c2\u6570\u8bbe\u7f6e", None))
        self.comboBox_scale.setItemText(0, QCoreApplication.translate("MainWidget", u"1920\u00d71080", None))
        self.comboBox_scale.setItemText(1, QCoreApplication.translate("MainWidget", u"1280\u00d7720", None))

        self.label_src_path.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9\u89c6\u9891\u8def\u5f84:", None))
        self.label_target_path.setText(QCoreApplication.translate("MainWidget", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84:", None))
        self.label_audio_bitrate.setText(QCoreApplication.translate("MainWidget", u"\u97f3\u9891\u6bd4\u7279\u7387", None))
        self.comboBox_audio_bitrate.setItemText(0, QCoreApplication.translate("MainWidget", u"128k", None))
        self.comboBox_audio_bitrate.setItemText(1, QCoreApplication.translate("MainWidget", u"192k", None))
        self.comboBox_audio_bitrate.setItemText(2, QCoreApplication.translate("MainWidget", u"256k", None))
        self.comboBox_audio_bitrate.setItemText(3, QCoreApplication.translate("MainWidget", u"512k", None))

        self.label_audio_codec.setText(QCoreApplication.translate("MainWidget", u"\u97f3\u9891\u7f16\u7801\u683c\u5f0f", None))
        self.comboBox_audio_codec.setItemText(0, QCoreApplication.translate("MainWidget", u"aac", None))
        self.comboBox_audio_codec.setItemText(1, QCoreApplication.translate("MainWidget", u"ogg", None))
        self.comboBox_audio_codec.setItemText(2, QCoreApplication.translate("MainWidget", u"mp3", None))

        self.label_preset.setText(QCoreApplication.translate("MainWidget", u"\u7f16\u7801\u901f\u5ea6", None))
        self.comboBox_preset.setItemText(0, QCoreApplication.translate("MainWidget", u"ultrafast", None))
        self.comboBox_preset.setItemText(1, QCoreApplication.translate("MainWidget", u"superfast", None))
        self.comboBox_preset.setItemText(2, QCoreApplication.translate("MainWidget", u"veryfast", None))
        self.comboBox_preset.setItemText(3, QCoreApplication.translate("MainWidget", u"faster", None))
        self.comboBox_preset.setItemText(4, QCoreApplication.translate("MainWidget", u"fast", None))
        self.comboBox_preset.setItemText(5, QCoreApplication.translate("MainWidget", u"medium", None))
        self.comboBox_preset.setItemText(6, QCoreApplication.translate("MainWidget", u"slow", None))
        self.comboBox_preset.setItemText(7, QCoreApplication.translate("MainWidget", u"slower", None))
        self.comboBox_preset.setItemText(8, QCoreApplication.translate("MainWidget", u"veryslow", None))

        self.label_video_fade_time.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u9000\u51fa\u6e10\u9690\u65f6\u95f4", None))
        self.label_audio_fade_time.setText(QCoreApplication.translate("MainWidget", u"\u9000\u51fa\u97f3\u9891\u6e10\u9690\u65f6\u95f4", None))
        self.label_start_time.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u5f00\u5934\u65f6\u95f4", None))
        self.label_effect_config.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u6548\u679c\u8bbe\u7f6e", None))
        self.doubleSpinBox_start_time.setPrefix("")
        self.label_end_time.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u7ed3\u5c3e\u65f6\u95f4", None))
        self.label_scale_size.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u7f29\u653e\u500d\u7387", None))
        self.doubleSpinBox_scale_size.setPrefix("")
        self.doubleSpinBox_scale_size.setSuffix(QCoreApplication.translate("MainWidget", u"%", None))
        self.label_condition.setText(QCoreApplication.translate("MainWidget", u"\u89c6\u9891\u5904\u7406\u8fdb\u5ea6", None))
        self.label_condition_name.setText(QCoreApplication.translate("MainWidget", u"\u5f85\u5f00\u59cb", None))
    # retranslateUi

