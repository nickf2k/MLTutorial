import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

np.random.seed(11)
means = [[2,2],[8,3],[3,6]]
cov = [[1,0],[0,1]]
N= 500
X0 = np.random.multivariate_normal(means[0],cov,N)
X1 = np.random.multivariate_normal(means[1],cov,N)
X2 = np.random.multivariate_normal(means[2],cov,N)
X= np.concatenate((X0,X1,X2),axis=0)
K = 3
origin_label = np.asarray([0]*N + [1]* N + [2]*N).T
def kmean_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label==0, :]
    X1 = X[label==1, :]
    X2 = X[label==2, :]
    plt.plot(X0[:,0])