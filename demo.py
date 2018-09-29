#!user/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-09-29 15:56:29
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-09-29 19:29:31

from DFauto import DFAuto
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal
import threading
from DFdemoUI import Ui_Dialog
import time


class MainWindow(QtGui.QDialog,threading.Thread):

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.DF = DFAuto(self.ui.Edit_ip.text(),int(self.ui.Edit_port.text()))
        threading.Thread.__init__(self)
        self.setDaemon(True)

        self.device_field = ['wiper_f','wiper_r','lamp_near','lamp_far','foglamp_f',
                            'loclamp','siglamp_l','siglamp_r','alarmlamp','brakelamp',
                            'reverselamp','warninglamp','foglamp_r']
        self.driver_field = ['enable_auto','brake']


    def run(self):
        while True:
            for name in self.device_field:
                exec('self.DF.device.%s=int(self.ui.checkBox_%s.isChecked())'%(name,name))
            for name in self.driver_field:
                exec('self.DF.driver.%s=int(self.ui.checkBox_%s.isChecked())'%(name,name))

            self.DF.driver.gas = self.ui.Slider_gas.value()
            self.DF.driver.steering_wheel = self.ui.Slider_wheel.value()
            self.DF.driver.deceleration = self.ui.Slider_deceleration.value()
            self.DF.driver.steering_vel = self.ui.Slider_wheel_vel.value()
            buf = self.DF.upload()
            self.ui.device_signal.emit(repr(buf['device']))
            self.ui.driver_signal.emit(repr(buf['driver']))
            time.sleep(0.1)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    myapp.start()
    app.exec_()