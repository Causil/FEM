import numpy as np
from sys import path 
path.append('..\\Data2D')

import Data2D\coordenadas_1
data = np.loadtxt(fname = 'coordenadas_1.dat', dtype = float)
print(data)

print('Hola mundo')
