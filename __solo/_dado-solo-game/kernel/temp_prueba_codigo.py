from typing import Tuple, Literal
from random import randint

list_dtipo = Literal['f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp']
tipo_dim = Tuple[int, int]
vg_dtipo = ('f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp')
vg_dparametros = {        # tipo de dado <-> parámetros para la creación
    'f1': ((1,5), (3,3), (0,1,0,1,1,1,0,1,0), 5),
    'f2': ((1,6), (4,3), (0,1,0,1,1,1,0,1,0,0,1,0), 6),
    'f3': ((1,6), (3,4), (0,1,0,0,1,1,1,1,0,1,0,0), 6),
    'f1*': (3,3),
    'f2*': (4,3),
    'f3*': (3,4)
}

def _valDim(dim: tipo_dim,
            forma: list_dtipo = None,
            posic_v: Tuple = None,
            n_caras: int = None
            ):
    """Validación para dimensión del dado
    La dimensión tiene que ser una tupla de enteros positivos.
    La dimensión la podemos validar con respecto a la forma,
    con respecto a la posición de los valores o al número de caras.

    (!) Orden de prioridad: forma -> posición -> n_caras 
    
    OUTPUT:
    -------
    Se ajusta al parámetro"""
    
    # Validación según la forma
    if type(dim) != tuple or len(dim) != 2: dim = (3,3)
    if len(dim) == 2 and type(dim[0]) == int and dim[0] > 0 and type(dim[1]) == int and dim[1] > 0: dim = (3,3)
    
    # Validación con respecto a la forma:
    if forma != None:
        for c, v in vg_dparametros.items():
            if c == forma:
                if len(v) > 2: return v[1]
                else: return v
        return dim

    # Validación según la posición
    if posic_v != None:
        if len(posic_v) == dim[0] * dim[1]: return dim
        else:
            n = len(posic_v)
            # Buscar los factores primos de la longitud de posic_v
            i = 2
            factores = []
            while i * i <= n:
                while n % i == 0: 
                    factores.append(i)
                    n //= i
                i += 1
            if n > 1:
                factores.append(n)
            
            # Reducción de la lista de factores primos a una lista de tamaño
            i = randint(1, len(factores) - 1)
            t_dim = [1,1]
            for indice, valor in enumerate(factores):
                if indice < i: t_dim[0] = valor * t_dim[0]
                else: t_dim[1] = valor * t_dim[1]
            dim = tuple(t_dim)

            return dim
    
    # Validación según el número de caras
    


print(_valDim((), posic_v=(0,1,0,1,1,1,0,1,0,0,1,0)))