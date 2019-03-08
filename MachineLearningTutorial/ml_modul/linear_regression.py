from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
x= np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).T
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
#show data
plt.plot(x,y,'ro')
plt.axis([140, 190, 45, 75])
plt.xlabel("height")
plt.ylabel("weight")
plt.show()