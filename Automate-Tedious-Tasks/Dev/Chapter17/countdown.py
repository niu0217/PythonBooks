#!python3
# -*- coding: utf-8 -*-

"""
countdown.py

一个简单的计时器。

该模块包含以下功能：
1. 倒计时60s
2. 结束播放声音

Author: niu0217
Date: 2023-12-20
"""

import time
import subprocess

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left -= 1

subprocess.Popen(['open', 'sources/alarm.wav'])
