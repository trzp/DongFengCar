#!user/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-09-28 12:03:44
# Contact: mrtang@nudt.edu.cn
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-09-28 17:21:32

# note: this script matches the protocol of DongFen auto car
#      protocol is provided by Pro. Liu

import numpy as np
import socket
import time
from struct import pack
import threading

# 确认字节顺序，确认校验时是否包含包头,需不需要频繁发送信息


class ElectricDevice:
    def __init__(self):
        self.reset()

    def reset(self):
        self.counter = 0
        self.wiper_f = 0
        self.wiper_r = 0
        self.lamp_near = 0
        self.lamp_far = 0
        self.foglamp_f = 0
        self.foglamp_r = 0
        self.loclamp = 0
        self.siglamp_l = 0
        self.siglamp_r = 0
        self.alarmlamp = 0
        self.brakelamp = 0
        self.reverselamp = 0
        self.warninglamp = 0
        self.status = 0
        self.longitude = 0
        self.latitude = 0
        self._ch = 0

    def tobuf(self):
        buf = np.array([130], dtype=np.uint8).tostring()
        buf += np.array([self.counter],
                        dtype=np.uint16).tostring()[::-1]  # 注意编码字节顺序
        buf += np.array([self.wiper_f, self.wiper_r, self.lamp_near, self.lamp_far, self.foglamp_r, self.foglamp_f,
                         self.loclamp, self.siglamp_l, self.siglamp_r, self.alarmlamp, self.brakelamp, self.reverselamp,
                         self.warninglamp, self.status], dtype=np.uint8).tostring()
        buf += np.array([self.longitude],
                        dtype=np.uint32).tostring()[::-1]  # 注意编码字节顺序
        buf += np.array([self.latitude],
                        dtype=np.uint32).tostring()[::-1]  # 注意编码字节顺序
        ch = np.array([sum(np.fromstring(buf, dtype=np.uint8))],
                      dtype=np.uint8).tostring()
        buf += ch
        return buf


class Driver:
    def __init__(self):
        self.reset()

    def reset(self):
        self.enable_auto = 0
        self.counter = 0
        self.gas = 0
        self.steering_wheel = 0
        self.steering_vel = 5
        self.brake = 0
        self.deceleration = 0

    def tobuf(self):
        buf = pack('B', 128)
        buf += pack('>i', self.counter)[-2:]
        buf += pack('B', self.enable_auto)
        buf += pack('>f', self.gas)  # 注意确定字节顺序
        buf += pack('>f', self.steering_wheel)
        buf += pack('i', self.steering_vel)[:2]
        buf += pack('B', self.brake)
        buf += pack('>f', self.deceleration)
        return buf


class DFAuto:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.device = ElectricDevice()
        self.driver = Driver()

    def upload(self):
        buf1 = self.device.tobuf()
        buf2 = self.driver.tobuf()
        self.s.sendto(buf1,self.addr)
        time.sleep(0.01)
        self.s.sendto(buf2,self.addr)

class DFauto2(threading.Thread,DFAuto):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        DFAuto.__init__(self,ip,port)

    def run(self):
        while True:
            self.upload()
            time.sleep(0.1)


if __name__ == '__main__':
    acar = DFauto2('127.0.0.1', 9000)
    acar.start()
    while True:
        acar.device.lamp_near = raw_input('cmd')
        print 'yes'

