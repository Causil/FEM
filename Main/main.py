from sys import path 
path.append('../Utils')
import utils as u
from numpy import loadtxt 

coordinates = loadtxt(fname = '../Data2D/coordenadas_1.dat', dtype = float)
elements = loadtxt(fname = '../Data2D/elementos_1.dat', dtype = float)
A = u.RigidexMatrix(coordinates, elements)
print(A)