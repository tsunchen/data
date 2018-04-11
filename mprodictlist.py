#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/4/11 07:10
py3
"""

import os
import multiprocessing
import time






def func(mdict, mlist):
	mdict["Anna"] = "Annaris"
	mdict["Beri"] = "Berilli"
	mlist.append(11)
	mlist.append(22)
	mlist.append(33)
 	#print (num.value)



if __name__=="__main__":

	# 
	# subpro put, one mainpro get

	with multiprocessing.Manager() as MG:
		mdict = multiprocessing.Manager().dict()
		mlist = multiprocessing.Manager().list(range(5))

	p=multiprocessing.Process(target=func, args=(mdict,mlist))
	p.start()
	p.join()

	print (mdict)
	print (mlist)


	print ("fin--")
