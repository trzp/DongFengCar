#!user/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-09-28 17:11:13
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-09-28 17:12:51

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9000))
while True:
    data,addr = s.recvfrom(128)
    print data