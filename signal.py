#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/04/05 20:10

[root@tsunz processtest]# python signal.py
"""

import subprocess
import signal

def isOut(signum, frame):
    print ("signal is end")

signal.signal(signal.SIGINT, isOut)

pingP = subprocess.Popen(args=["ping www.google.com"], shell=True)
pingP.wait()
print(pingP.pid)
print(pingP.returncode)
