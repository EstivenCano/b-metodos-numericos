#Recibe una ecuacion, un punto xy inicial, la x final que es lo que se va a buscar y una h que seria la longitud de salto
def runge_kutta_4(f,x0,y0,xf,h):
    #Pasamos a float lo que viene como string
    x0 = float(x0)
    y0 = float(y0)
    xf = float(xf)
    h = float(h)

    #Se hacen dos arreglos para guardar los puntos resultantes
    x = [x0]
    y = [y0]
    ySiguiente = 0
    err = 0

    salto = x0
    i = 0
    while (salto <= (xf - h)):
      
      k1 = f(x[i], y[i])
      k2 = f( ( x[i] + (h/2) ), ( y[i] + (k1*h / 2) ) )
      k3 = f( ( x[i] + (h/2) ), ( y[i] + (k2*h / 2) ) )
      k4 = f( ( x[i] + (h) ), ( y[i] + (k3*h) ) )

      ySiguiente = y[i] + (h/6)*( k1 + 2*k2 + 2*k3 + k4 )
      y.append(ySiguiente)
      salto += h
      x.append(salto)
      i += 1
    err = 1
    return x, y, err

#Runge kutta de orden superior
def runge_kutta_ordenS(f, x0, y0, xf, h):
    #Pasamos a float lo que viene como string
    x0 = float(x0)
    y0 = float(y0)
    xf = float(xf)
    h = float(h)
    #Arreglos para guardar los puntos que vamos calculando
    x = [x0]
    y = [y0]
    ySiguiente = 0
    err = 0

    salto = x0
    i = 0
    while (salto <= (xf - h)):
      k1 = f( x[i], y[i] )
      k2 = f( ( x[i] + ( 1/4 * h ) ), ( y[i] + ( 1/4 * k1 * h) ) )
      k3 = f( ( x[i] + ( 1/4 * h ) ), ( y[i] + (1/8 * k1 * h) + (1/8 * k2 * h) ) )
      k4 = f( ( x[i] + ( 1/2 * h ) ), ( y[i] - (1/2 * k2 * h) + k2 * h ) )
      k5 = f( ( x[i] + ( 3/4 * h ) ), ( y[i] - (3/16 * k1 * h) + ( 9/16 * k4 * h ) ) )
      k6 = f( ( x[i] + h ), ( y[i] - (3/7 * k1 * h) + ( 12/7 * k3 * h ) - ( 12/7 * k4 * h ) + ( 8/7 * k5 * h ) ) )

      ySiguiente = y[i] + ( (1/90) * (7*k1 + 32 * k3 + 12 * k4 + 32 * k5 + 7 * k6) * h )

      y.append(ySiguiente)
      salto += h
      x.append(salto)
      i += 1
    err = error(y[-1], y[-2])
    return x, y, err

def error(actual, anterior):
    return abs(((actual - anterior) / actual) * 100)