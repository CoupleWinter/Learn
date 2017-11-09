# -*- coding: utf-8 -*-
import matplotlib
matplotlib.matplotlib_fname()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# 每次产生一个新的坐标点
def data_gen():
  t = data_gen.t
  cnt = 0
  while cnt < 1000:
    cnt+=1
    t += 0.05
    yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
data_gen.t = 0
# 绘图
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 5)
ax.grid()
xdata, ydata = [], []
# 因为run的参数是调用函数data_gen,
# 所以第一个参数可以不是framenum:设置line的数据,返回line
def run(data):
  # update the data
  t,y = data
  xdata.append(t)
  ydata.append(y)
  xmin, xmax = ax.get_xlim()
  if t >= xmax:
    ax.set_xlim(xmin, 2*xmax)
    ax.figure.canvas.draw()
  line.set_data(xdata, ydata)
  return line,
# 每隔10秒调用函数run,run的参数为函数data_gen,
# 表示图形只更新需要绘制的元素
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
  repeat=False)
plt.show()

"""
Demo of the streamplot function with masking.

This example shows how streamlines created by the streamplot function skips
masked regions and NaN values.
"""
import numpy as np
import matplotlib.pyplot as plt

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

mask = np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask=mask)

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, color='r')

ax.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5,
          interpolation='nearest', cmap=plt.cm.gray)

plt.show()

import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()