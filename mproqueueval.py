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






def func(num):
	num.value=10.9
	#print (num.value)



if __name__=="__main__":

	# 
	# subpro put, one mainpro get

	num = multiprocessing.Value("d", 10.0)
	print (num.value)
	p=multiprocessing.Process(target=func, args=(num,))
	p.start()
	p.join()

	print (num.value)


	print ("fin--")
