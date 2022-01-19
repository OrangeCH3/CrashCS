#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022/1/19 22:19
# @File     : 0-赛博朋克.py
# @Project  : main.py


import numpy as np
import mplcyberpunk
import matplotlib.pyplot as plt

plt.style.use("cyberpunk")

# 数据
x = np.arange(-7, 7, 0.1)

y1 = np.sin(x)
y2 = np.sin(x) + x
y3 = np.sin(x) * x
y4 = np.sin(x) / x

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

# 线条发光
mplcyberpunk.make_lines_glow()
# 面积图
mplcyberpunk.add_underglow()

plt.show()
