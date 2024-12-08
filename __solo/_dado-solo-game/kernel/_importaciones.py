
from typing import Literal, Callable, Tuple
from random import randint, sample


f_dado = Literal['f1','f2', 'f3']           # Formas del dado
dir_mv = Literal['u', 'd', 'r', 'l']        # Dirección del movimiento

# Variables globales
fd_rvalor = {        # forma del dado <-> rango de valores de las caras
    'f1': ((3,3), (0,1,0,1,1,1,0,1,0), (1,5)),
    'f2': ((4,3), (0,1,0,1,1,1,0,1,0,0,1,0), (1,6)),
    'f3': ((3,4), (0,1,0,0,1,1,1,1,0,1,0,0), (1,6))
}