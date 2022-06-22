from numpy import zeros, array, append, linalg, cross, ix_
#import numpy as np

def RigidexMatrix(coordinates, elements):
    numberCoordenates = len(coordinates)
    numberElements = len(elements)
    A = zeros((numberCoordenates,numberCoordenates),float)
    for element in elements:
        indexElement = (array(element)-1).astype(int)
        nodes =  coordinates[indexElement]
        Matcoef =  append(nodes,[[1],[1],[1]],axis=1)
        C = linalg.inv(Matcoef) #constantes de funciones bases
        a = append(nodes[1]-nodes[0],0)
        b = append(nodes[2]-nodes[0],0)
        area = 0.5*linalg.norm(cross(a,b))
        Grad = append(C[0:2],[[0,0,0]],axis=0)
        Mele = area*Grad.transpose()*Grad
        A[ix_(indexElement,indexElement)] = A[ix_(indexElement,indexElement)] + Mele
    return A

def gauss(n):
    x = zeros(n,1)
    w = x
    m = (n+1)/2
    for i in range(1,m+1):
        pass


def lado_derecho(ng,mode,coordenates,elements):
    numberCoordenates = len(coordenates)
    numberElements = len(elements)
    A = zeros()

#if __name__ == "__main__":
#	print("I prefer to be a module")