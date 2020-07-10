# 1 - simple plot
"""
Please note, this script is for python3+.
"""
# Youtube video tutorial: https://www.youtube.com/watch?v=4Y7f0znUT6E&list=PLXO45tsB95cKiBRXYqNNCw8AUo6tYen3l&index=3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1 #直線方程式
# y = x**2  #U形圖
plt.plot(x, y)
plt.show()
