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
import time


def info(title):
	print (title)
	time.sleep(2)
	print (__name__)
	print ("father ppid", os.getppid())
	print ("self pid", os.getpid())
	print ("---- ---- ---- ----")

if __name__=="__main__":
	info("start test up...")
	p1 = multiprocessing.Process(target=info, args=("20180406A",))
	
	p2 = multiprocessing.Process(target=info, args=("20180406B",))
	
	p3 = multiprocessing.Process(target=info, args=("20180406C",))
	
	p3.start()
	p2.start()
	p1.start()

	p1.join()
	p2.join()
	p3.join()
	print ("all fin")
