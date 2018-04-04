#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/04/04 12:10
"""

import pywifi
import pytest
import sys
import time
import platform
import logging
from pywifi import const

pywifi.set_loglevel(logging.INFO)

def test_disconnect():
	wifi = pywifi.PyWiFi()
	iface = wifi.interfaces()[0]
	iface.disconnect()
	assert iface.status() in \
	    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]


def test_connect():
	wifi = pywifi.PyWiFi()
	iface = wifi.interfaces()[0]
	iface.disconnect()
	time.sleep(1)
	assert iface.status() in \
	    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
	profile = pywifi.Profile()
	profile.ssid = 'sjhl'
	profile.auth = const.AUTH_ALG_OPEN
	profile.akm.append(const.AKM_TYPE_WPA2PSK)
	profile.cipher = const.CIPHER_TYPE_CCMP
	profile.key = '21viacloud123;'
	iface.remove_all_network_profiles()
	tmp_profile = iface.add_network_profile(profile)
	iface.connect(tmp_profile)
	time.sleep(10)
	isConn = 0 #assert iface.status() == const.IFACE_CONNECTED
	if iface.status() == const.IFACE_CONNECTED:
		isConn = 1
		#print (isConn)
		print ("Successfully linked.")
	iface.disconnect()
	if isConn:
		return isConn
	time.sleep(1)#assert iface.status() in \#    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
	if iface.status() in  [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
		print ("Fail to link")
	return isConn


def test_interfaces():
	wifi = pywifi.PyWiFi()

	assert wifi.interfaces()

	if platform.system().lower() == 'windows':
		assert wifi.interfaces()[0].name() == \
		    '1x1 11b/g/n Wireless LAN PCI Express Half Mini Card Adapter'
	elif platform.system().lower() == 'linux':
		assert wifi.interfaces()[0].name() == 'wlx'

def test_scan():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)
    bsses = iface.scan_results()
    for data in bsses:
        print (data)



print  (test_connect())
test_interfaces()
test_scan()
test_disconnect()
