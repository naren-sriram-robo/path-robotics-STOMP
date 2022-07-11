from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import csv
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
print("y shape:",y.shape)
print("x old shape:",x.shape)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=41, endpoint=True)
print("xnew shape:",xnew.shape,"f shape:",f(x).shape)
plt.plot(x, y, 'o', x, f(x), '-', x, f2(x), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()