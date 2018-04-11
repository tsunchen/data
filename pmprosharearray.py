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
	num[2]=10
	#print (num.value)



if __name__=="__main__":

	# 
	# subpro put, one mainpro get

	num = multiprocessing.Array("i", [1,2,3,4,5])
	print (num[:])
	p=multiprocessing.Process(target=func, args=(num,))
	p.start()
	p.join()

	print (num[:])


	print ("fin--")
