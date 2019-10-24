import matplotlib.pyplot as plt
from pylab import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
from  matplotlib.figure import Figure
import numpy as np

#line plot - kieu lien
# plt.plot(np.random.randint(20, size=100)) #1 vector 1d, co 100 gia tri < 20
# plt.show()

#scatter plot- do thi kieu roi rac
# x = np.random.randn(300)
# y = np.random.randn(300)
# # plt.plot(x,y,"ob")
# plt.scatter(x,y)
# plt.show()

#bar chart
y = [3,5,10,2,1,9,6]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x,y,width,color = "blue")
plt.show()

