#!/usr/local/bin/python3

# import math
# import matplotlib
# matplotlib.use('TkAgg')
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
#
# def beta_pdf(x, a, b):
#     return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
#             / (math.gamma(a) * math.gamma(b)))
#
#
# class UpdateDist(object):
#     def __init__(self, ax, prob=0.5):
#         self.success = 0
#         self.prob = prob
#         self.line, = ax.plot([], [], 'k-')
#         self.x = np.linspace(0, 1, 200)
#         self.ax = ax
#
#         # Set up plot parameters
#         self.ax.set_xlim(0, 1)
#         self.ax.set_ylim(0, 15)
#         self.ax.grid(True)
#
#         # This vertical line represents the theoretical value, to
#         # which the plotted distribution should converge.
#         self.ax.axvline(prob, linestyle='--', color='black')
#
#     def init(self):
#         self.success = 0
#         self.line.set_data([], [])
#         return self.line,
#
#     def __call__(self, i):
#         # This way the plot can continuously run and we just keep
#         # watching new realizations of the process
#         if i == 0:
#             return self.init()
#
#         # Choose success based on exceed a threshold with a uniform pick
#         if np.random.rand(1,) < self.prob:
#             self.success += 1
#         y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
#         self.line.set_data(self.x, y)
#         return self.line,
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# fig, ax = plt.subplots()
# ud = UpdateDist(ax, prob=0.7)
# anim = FuncAnimation(fig, ud, frames=np.arange(100), init_func=ud.init,
#                      interval=100, blit=True)
# plt.show()


# from nltk import *
# import matplotlib
# matplotlib.use('tkagg')
# hi = ['f','f','u','c','k']
#
# kk = FreqDist(hi)
# kk.plot()
# print(kk)
#
# import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro', animated=True)
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()



import comment_level
keys = list(comment_level.level.keys())
values = list(comment_level.level.values())
values.reverse()
keys.reverse()
'''
饼状图绘画
'''
#
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = keys
sizes = values
explode = (0.1, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


'''
柱形图绘画
'''
# import matplotlib.pyplot as plt
# x = keys
# y = values
# plt.ylabel('数量')
# plt.xlabel('等级')
# plt.bar(x,y)
# plt.show()