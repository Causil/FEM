import numpy as np
from sys import path 
path.append('../MatrixRigidex')
import RigidexMatrix as rg
coordinates = np.loadtxt(fname = '../Data2D/coordenadas_1.dat', dtype = float)
elements = np.loadtxt(fname = '../Data2D/elementos_1.dat', dtype = float)
A = rg.RigidexMatrix(coordinates, elements)
print(A)