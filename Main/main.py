import numpy as np
from sys import path 
#path.append('..\\Data2D')
coordinates = np.loadtxt(fname = '../Data2D/coordenadas_1.dat', dtype = float)
elements = np.loadtxt(fname = '../Data2D/elementos_1.dat', dtype = float)


def RigidezMatrix(coordinates, elements):
    numberCoordenates = len(coordinates)
    numberElements = len(elements)
    A = np.zeros((numberCoordenates,numberCoordenates),float)
    for element in elements:
        indexElement = (np.array(element)-1).astype(int)
        nodes =  coordinates[indexElement]
        Matcoef =  np.append(nodes,[[1],[1],[1]],axis=1)
        C = np.linalg.inv(Matcoef) #constantes de funciones bases
        a = np.append(nodes[1]-nodes[0],0)
        b = np.append(nodes[2]-nodes[0],0)
        area = 0.5*np.linalg.norm(np.cross(a,b))
        Grad = np.append(C[0:2],[[0,0,0]],axis=0)
        Mele = area*Grad.transpose()*Grad
        A[np.ix_(indexElement,indexElement)] = A[np.ix_(indexElement,indexElement)] + Mele
    return A
A = RigidezMatrix(coordinates, elements)
print(A)