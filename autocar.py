#!user/bin/python
# -*-coding:utf-8-*-

#FileName: autocar.py
#Version: 1.0
#Author: Jingsheng Tang
#Date: 2018/09/13
#Email: mrtang@nudt.edu.cn
#Github: trzp

#note: this script matches the protocol of DongFen auto car
#      protocol is provided by Pro. Liu

import numpy as np
import socket
import time

class AutoCar:
    def __init__(self,ip,port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.addr = (ip,port)
        self.resetall()

    def resetall(self):
        self.Enable_auto = 0
        self.Count1 = 0
        self.Gas = 0
        self.Steering_wheel = 0
        self.Steering_vel = 5
        self.Brake = 0
        self.Deceleration = 0

    def update1(self):
        buf = ''
        buf = buf + pack('!i',self.Count1)[-2:]
        buf = buf + pack('B',self.Enable_auto)
        buf = buf + pack('f',self.Gas)
        buf = buf + pack('f',self.Steering_wheel)
        buf = buf + pack('i',self.Steering_vel)[:2]
        buf = buf + pack('B',self.Brake)
        buf = buf + pack('f',self.Deceleration)

        ay = sum(np.fromstring(buf,dtype=np.uint8))
        ch = pack('i',ay)[0]
        buf = pack('B',128)+buf+ch
        return buf
    
    def update2(self):
        return ''

    def send(self):
        buf1 = self.update1()
        buf2 = self.update2()
        self.s.sendto(buf1,self.addr)
        time.sleep(0.05)
        self.s.sendto(buf2,self.addr)

if __name__ = '__main__':
    acar = AutoCar('127.0.0.1',9000)
    acar.Enable_auto = 1
    acar.Gas = 100
    acar.send()
    
    time.sleep(10)
    acar.Gas = 0
    acar.Brake = 100
    acar.send()