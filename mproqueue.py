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

queue = multiprocessing.Queue()




def func(queue, i):
	queue.put(i)
	print("put", os.getpid(), i)



if __name__=="__main__":

	# 
	# subpro put, one mainpro get
	mprolist = []
	for i in range(10):
		p = multiprocessing.Process(target=func, args=(queue,i))
		p.start()
		mprolist.append(queue.get())
		p.join()

	print (mprolist)
	print ("fin--")
