#[root@tsunz processtest]# vi processsonfather.py

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2018/04/05 20:10
"""

import os

print ("Process Test startup...")

pid = os.fork()
print ("a is boy")
print ("b is another one")
print (pid)

if pid == 0:
        print ("son process")
else:
        print ("father process")

