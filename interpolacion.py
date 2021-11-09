import numpy as np

#Metodo de lagrange cuando se tienen solo los puntos
def lagrange_general(x, y,busq):    
  Px = 0

  for k in range(len(x)):
      for i in range(len(y)):  
          if i != k:
              Px = Px + (((float(busq) - float(x[i])) / (float(x[k]) - float(x[i]))) * float(y[k]))
  return Px

def error(real, calculado):
    return ((real - calculado) / real) * 100

def diferenciasDivididad(x, y):

    n = len(y)
    diferencias = np.zeros([n, n])

    # Asigna a y en la primera columna
    diferencias[:,0] = y
    
    # Ya tiene asignala la primera como y, empieza desde la segunda
    for j in range(1,n):
        for i in range(n-j):
          # Divide las diferencias anteriores por las actuales
            diferencias[i][j] = (diferencias[i+1][j-1] - diferencias[i][j-1]) / (float(x[i+j])-float(x[i]))
            
    return diferencias

def polinomio_newton(grado, x, y, X):
    
    diferencias = diferenciasDivididad(x,y)
    prodAux = 1
    resultado = diferencias[0, 0]
    for i in range(grado):
        prodAux *= (float(X) - float(x[i]))
        resultado += prodAux * diferencias[0, i+1]
    
    return resultado