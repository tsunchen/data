#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/02/15 09:10
"""

import os


#f*=(p*rW-q*rL)/（rLrW）
'''
f* 为现有资金应进行下次投注的比例；
b 为投注可得的赔率（此处的赔率是净赔率）；
p 为获胜率；

rW是获胜后的净赢率;
rL是净损失率;
'''

def kellycriterion(p, rW, rL=1):
	kc_f = 0
	#print (float(18)/38)
	p = float(p)
	print "p = %s" % p
	q = 1 - p
	print "q = %s" % q
	rW = rW
	print "b = %s" % rW
	rL = rL
	kc_f = (p*rW - q*rL) / (rL * rW)
	print "%6.6f" % kc_f
	return kc_f



if __name__=='__main__':
	#print kellycriterion(0.4, 0.3, 0.1)
	print kellycriterion(0.4, 2)
	print kellycriterion((float(18)/38), 1)
	print kellycriterion((float(5)/10), 1)
	print kellycriterion((float(1)/1), 1)


