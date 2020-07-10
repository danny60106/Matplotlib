# 4 - figure

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50) 
#從-3~3生成50個點來畫

y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)

plt.figure(figsize=(8, 5))
plt.plot(x, y2)

# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()
