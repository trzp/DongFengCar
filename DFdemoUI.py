# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DFdemo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal,QObject

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QObject):

    #自定义信号
    device_signal = pyqtSignal(str)
    driver_signal = pyqtSignal(str)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(488, 486)
        Dialog.setMinimumSize(QtCore.QSize(488, 486))
        Dialog.setMaximumSize(QtCore.QSize(488, 486))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 471))
        self.verticalLayoutWidget.setObjectName(
            _fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.Edit_port = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Edit_port.setObjectName(_fromUtf8("Edit_port"))
        self.gridLayout.addWidget(self.Edit_port, 1, 3, 1, 1)
        self.Edit_ip = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.Edit_ip.setObjectName(_fromUtf8("Edit_ip"))
        self.gridLayout.addWidget(self.Edit_ip, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.Edit_device = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.Edit_device.setFrameShadow(QtGui.QFrame.Plain)
        self.Edit_device.setObjectName(_fromUtf8("Edit_device"))
        self.verticalLayout_2.addWidget(self.Edit_device)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.Edit_driver = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.Edit_driver.setObjectName(_fromUtf8("Edit_driver"))
        self.verticalLayout_2.addWidget(self.Edit_driver)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_wiper_f = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_wiper_f.setEnabled(True)
        self.checkBox_wiper_f.setObjectName(_fromUtf8("checkBox_wiper_f"))
        self.gridLayout_2.addWidget(self.checkBox_wiper_f, 1, 0, 1, 1)
        self.checkBox_foglamp_r = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_foglamp_r.setObjectName(_fromUtf8("checkBox_foglamp_r"))
        self.gridLayout_2.addWidget(self.checkBox_foglamp_r, 1, 1, 1, 1)
        self.checkBox_loclamp = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_loclamp.setObjectName(_fromUtf8("checkBox_loclamp"))
        self.gridLayout_2.addWidget(self.checkBox_loclamp, 1, 2, 1, 1)
        self.checkBox_wiper_r = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_wiper_r.setObjectName(_fromUtf8("checkBox_wiper_r"))
        self.gridLayout_2.addWidget(self.checkBox_wiper_r, 2, 0, 1, 1)
        self.checkBox_foglamp_f = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_foglamp_f.setObjectName(_fromUtf8("checkBox_foglamp_f"))
        self.gridLayout_2.addWidget(self.checkBox_foglamp_f, 2, 1, 1, 1)
        self.checkBox_warninglamp = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_warninglamp.setObjectName(
            _fromUtf8("checkBox_warninglamp"))
        self.gridLayout_2.addWidget(self.checkBox_warninglamp, 2, 2, 1, 1)
        self.checkBox_lamp_near = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_lamp_near.setObjectName(_fromUtf8("checkBox_lamp_near"))
        self.gridLayout_2.addWidget(self.checkBox_lamp_near, 3, 0, 1, 1)
        self.checkBox_siglamp_l = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_siglamp_l.setObjectName(_fromUtf8("checkBox_siglamp_l"))
        self.gridLayout_2.addWidget(self.checkBox_siglamp_l, 3, 1, 1, 1)
        self.checkBox_brakelamp = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_brakelamp.setObjectName(_fromUtf8("checkBox_brakelamp"))
        self.gridLayout_2.addWidget(self.checkBox_brakelamp, 3, 2, 1, 1)
        self.checkBox_lamp_far = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_lamp_far.setObjectName(_fromUtf8("checkBox_lamp_far"))
        self.gridLayout_2.addWidget(self.checkBox_lamp_far, 4, 0, 1, 1)
        self.checkBox_siglamp_r = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_siglamp_r.setObjectName(_fromUtf8("checkBox_siglamp_r"))
        self.gridLayout_2.addWidget(self.checkBox_siglamp_r, 4, 1, 1, 1)
        self.checkBox_reverselamp = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_reverselamp.setObjectName(
            _fromUtf8("checkBox_reverselamp"))
        self.gridLayout_2.addWidget(self.checkBox_reverselamp, 4, 2, 1, 1)
        self.checkBox_alarmlamp = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_alarmlamp.setObjectName(_fromUtf8("checkBox_alarmlamp"))
        self.gridLayout_2.addWidget(self.checkBox_alarmlamp, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox_enable_auto = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_enable_auto.setObjectName(
            _fromUtf8("checkBox_enable_auto"))
        self.gridLayout_3.addWidget(self.checkBox_enable_auto, 1, 0, 1, 1)
        self.checkBox_brake = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_brake.setObjectName(_fromUtf8("checkBox_brake"))
        self.gridLayout_3.addWidget(self.checkBox_brake, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.label_gas = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_gas.setObjectName(_fromUtf8("label_gas"))
        self.horizontalLayout.addWidget(self.label_gas)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.label_wheel = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_wheel.setObjectName(_fromUtf8("label_wheel"))
        self.horizontalLayout.addWidget(self.label_wheel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Slider_gas = QtGui.QSlider(self.verticalLayoutWidget)
        self.Slider_gas.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_gas.setObjectName(_fromUtf8("Slider_gas"))
        self.horizontalLayout_3.addWidget(self.Slider_gas)
        self.Slider_wheel = QtGui.QSlider(self.verticalLayoutWidget)
        self.Slider_wheel.setMinimum(-50)
        self.Slider_wheel.setMaximum(50)
        self.Slider_wheel.setProperty("value", 0)
        self.Slider_wheel.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_wheel.setObjectName(_fromUtf8("Slider_wheel"))
        self.horizontalLayout_3.addWidget(self.Slider_wheel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.label_gas_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_gas_3.setObjectName(_fromUtf8("label_gas_3"))
        self.horizontalLayout_6.addWidget(self.label_gas_3)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.label_wheel_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_wheel_3.setObjectName(_fromUtf8("label_wheel_3"))
        self.horizontalLayout_6.addWidget(self.label_wheel_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.Slider_wheel_vel = QtGui.QSlider(self.verticalLayoutWidget)
        self.Slider_wheel_vel.setSliderPosition(10)
        self.Slider_wheel_vel.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_wheel_vel.setObjectName(_fromUtf8("Slider_wheel_vel"))
        self.horizontalLayout_5.addWidget(self.Slider_wheel_vel)
        self.Slider_deceleration = QtGui.QSlider(self.verticalLayoutWidget)
        self.Slider_deceleration.setMinimum(0)
        self.Slider_deceleration.setMaximum(50)
        self.Slider_deceleration.setProperty("value", 5)
        self.Slider_deceleration.setSliderPosition(5)
        self.Slider_deceleration.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_deceleration.setObjectName(
            _fromUtf8("Slider_deceleration"))
        self.horizontalLayout_5.addWidget(self.Slider_deceleration)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Slider_gas, QtCore.SIGNAL(
            _fromUtf8("valueChanged(int)")), self.label_gas.setNum)
        QtCore.QObject.connect(self.Slider_wheel, QtCore.SIGNAL(
            _fromUtf8("valueChanged(int)")), self.label_wheel.setNum)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(
            _fromUtf8("pressed()")), self.slot_bt_pressed)
        QtCore.QObject.connect(self.Slider_wheel_vel, QtCore.SIGNAL(
            _fromUtf8("valueChanged(int)")), self.label_gas_3.setNum)
        QtCore.QObject.connect(self.Slider_deceleration, QtCore.SIGNAL(
            _fromUtf8("valueChanged(int)")), self.label_wheel_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #自定义信号的连接
        self.device_signal.connect(self.device_show)
        self.driver_signal.connect(self.driver_show)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "通讯接口", None))
        self.label_3.setText(_translate("Dialog", "IP:", None))
        self.label_4.setText(_translate("Dialog", "Port:", None))
        self.Edit_port.setText(_translate("Dialog", "9000", None))
        self.Edit_ip.setText(_translate("Dialog", "127.0.0.1", None))
        self.label_7.setText(_translate("Dialog", "车声命令：", None))
        self.label_10.setText(_translate("Dialog", "控制命令：", None))
        self.label.setText(_translate("Dialog", "车身控制", None))
        self.checkBox_wiper_f.setText(_translate("Dialog", "前雨刷", None))
        self.checkBox_foglamp_r.setText(_translate("Dialog", "后雾灯", None))
        self.checkBox_loclamp.setText(_translate("Dialog", "位置灯", None))
        self.checkBox_wiper_r.setText(_translate("Dialog", "后雨刷", None))
        self.checkBox_foglamp_f.setText(_translate("Dialog", "前雾灯", None))
        self.checkBox_warninglamp.setText(_translate("Dialog", "危险报警灯", None))
        self.checkBox_lamp_near.setText(_translate("Dialog", "近光灯", None))
        self.checkBox_siglamp_l.setText(_translate("Dialog", "左转向灯", None))
        self.checkBox_brakelamp.setText(_translate("Dialog", "刹车灯", None))
        self.checkBox_lamp_far.setText(_translate("Dialog", "远光灯", None))
        self.checkBox_siglamp_r.setText(_translate("Dialog", "右转向灯", None))
        self.checkBox_reverselamp.setText(_translate("Dialog", "倒车灯", None))
        self.checkBox_alarmlamp.setText(_translate("Dialog", "警告灯", None))
        self.checkBox_enable_auto.setText(_translate("Dialog", "自动驾驶使能", None))
        self.checkBox_brake.setText(_translate("Dialog", "手刹控制", None))
        self.label_5.setText(_translate("Dialog", "运动控制", None))
        self.label_6.setText(_translate("Dialog", "油门量：", None))
        self.label_gas.setText(_translate("Dialog", "0", None))
        self.label_9.setText(_translate("Dialog", "方向：", None))
        self.label_wheel.setText(_translate("Dialog", "0", None))
        self.label_8.setText(_translate("Dialog", "方向盘转速：", None))
        self.label_gas_3.setText(_translate("Dialog", "10", None))
        self.label_11.setText(_translate("Dialog", "减速度：", None))
        self.label_wheel_3.setText(_translate("Dialog", "1", None))
        self.pushButton.setText(_translate("Dialog", "复位", None))

#   完成复位
    def slot_bt_pressed(self):
        for name, value in vars(self).items():
            if 'checkBox' in name:
                exec('self.%s.setChecked(False)' % (name))
        self.Slider_wheel.setValue(0)
        self.Slider_gas.setValue(0)
        self.Slider_deceleration.setValue(0)
        self.Slider_wheel_vel.setValue(5)

    def device_show(self, message):
        self.Edit_device.setText(message)

    def driver_show(self, message):
        self.Edit_driver.setText(message)


class MainWindow(QtGui.QDialog):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  # Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)


if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    app.exec_()
