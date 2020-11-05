import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)

mu = np.array([0, 0]) #mu
Sigma = np.array([[1, 0], [0, 1]]) #covariance matrix #case a: [[1, 0], [0, 1]], case b: [[4, 0], [0, 1]], case c: [[1, 0.5], [0.5, 1]], case b: [[1, -0.5], [-0.5, 1]]

pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

def multivariate_gaussian(pos, mu, Sigma):
    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma) #determinant
    Sigma_inv = np.linalg.inv(Sigma) #inverse
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)

    return np.exp(-fac / 2) / N

Z = multivariate_gaussian(pos, mu, Sigma)
plt.contourf(X, Y, Z, cmap='Blues')
plt.show()