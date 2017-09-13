# -*- coding:utf-8 -*-
"""
等高线图
"""
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    u = np.linspace(0, 4, 1000)
    x1, x2 = np.meshgrid(u, u)
    z = np.log(np.exp(x1) + np.exp(x2))
    # 针对数组z画一个等值线图，（x1, x2）确定面坐标，画20条等值线。
    plt.contourf(x1, x2, z, 20)
    plt.show()