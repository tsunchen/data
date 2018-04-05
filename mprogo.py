#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/4/6 07:10
py3
"""

import os
import multiprocessing


def info(title):
	print (title)
	print (__name__)
	print ("father ppid", os.getppid())
	print ("self pid", os.getpid())
	print ("---- ---- ---- ----")

if __name__=="__main__":
	info("start test up...")
	p = multiprocessing.Process(target=info, args=("20180406",))
	p.start()
	p.join()
	print ("hi fin")
