"""Contiene todas las piezas móviles del juego"""

from typing import Literal, Tuple, Callable
from random import sample, randint, choice

# Tipos de datos
list_dtipo = Literal['f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp']           # Tipos de dados según su forma
list_dir_mv = Literal['u', 'd', 'r', 'l']                                  # Dirección del movimiento
tipo_dim = Tuple[int, int]

# Variables globales
vg_dtipo = ('f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp')
vg_dtipo_b = ('f1','f2', 'f3')
vg_dtipo_e = ('f1*', 'f2*', 'f3*', 'fp')
vg_dparametros = {        # tipo de dado <-> parámetros para la creación
    'f1': ((1,5), (3,3), (0,1,0,1,1,1,0,1,0), 5),
    'f2': ((1,6), (4,3), (0,1,0,1,1,1,0,1,0,0,1,0), 6),
    'f3': ((1,6), (3,4), (0,1,0,0,1,1,1,1,0,1,0,0), 6),
    'f1*': (3,3),
    'f2*': (4,3),
    'f3*': (3,4)
}

# validaciones para los parámetros de creación de dados
def _valForma(forma: list_dtipo,                       # forma a validar
              dim: tipo_dim = None
              ):
    """Validación de la forma
    La forma tiene una estructura propia y aparte se puede validar con
    respecto a la dimensión.
    Devuelve la misma forma si es compatible con la dimensión o 
    devuelve la forma más compatible con la dimensión.
    
    (!) Se supone que la dim tiene una forma válida."""

    # Validación de forma
    if forma not in vg_dtipo: forma = 'fp'         # El valor no es valido => se pasa un valor genérico de forma
    
    # Validación con respecto a la dimensión
    for c, v in vg_dparametros.items():
        if len(v) > 2:
            if v[1] == dim and forma == c: return forma
            elif v[1] == dim: return c
        else:
            if v == dim and forma == c: return forma
            elif v == dim: return c

    return forma

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
        if len(posic_v) == dim[0]*dim[1]: return dim
        else:
            # Buscar los factores primos de la longitud de posic_v
            i = 2
            factores = []
            while i * i <= len(posic_v):
                if n % i: i+= 1
                else:
                    n //= i
                    factores.append(i)
    
    # Validación según el número de caras
    
            

def _valInterV(*, **deps):
    """Validación para intervalos de valores"""
    pass

def _valPosSec():
    """Validación para la posición de las caras en secuencia"""
    pass

def _valNumCaras():
    """Validación para el número de caras activas"""



class _PiezaMovil:
    """Clase abstracta
    Contiene toda la información común de las piezas móviles.
    """

    _estado: str = None
    coord: tuple[int,int] = None
    cantidad_caras: int = None
    cond_captura: int = None

    def _gCoord(self, 
                rango: int | Tuple[int, int]
                ) -> tuple[int, int]:   # Generador de coordenadas
        if type(rango) == int:
            return randint(1,rango), randint(rango)
        elif type(rango) == tuple and len(rango) == 2:
            return randint(rango[0], rango[1]), randint(rango[0], rango[1])
    
    def unPaso(self, 
               dir_mv: dir_mv = 'd'):
        print("Solo hago esto.")


class Dado(_PiezaMovil):
    """"""

    def __init__(self,
            *inter_v: int | Tuple[int,int],
            dtipo: list_dtipo = None,
            dim: Tuple[int,int] = None,
            posic_sec: Tuple = None,
            n_caras: int = None
        ) -> None:
        """"""

        self._inter_v = inter_v
        self._dtipo = dtipo
        self._dim = dim
        self._posic_sec = posic_sec
        self._n_caras = n_caras

        self.sec_valores = []
        self._matrix_valores = []

        # Caso 1: dtipo es básico
        if dtipo in vg_dtipo_b:
            # En caso de que no se pasen intervalos de valores
            if len(inter_v) == 0: self._inter_v = vg_dparametros[dtipo][0]
            # En caso de que se pasaran intervalos de valores
            elif len(inter_v) == 2:
                pass

            # No se permiten cambios de dimensión
            if dim != vg_dparametros[dtipo][1]: self._dim = vg_dparametros[dtipo][1]
            # No se permiten cambios de posición
            if posic_sec != vg_dparametros[dtipo][2]: self._posic_sec = vg_dparametros[dtipo][2]
            # No se permiten cambios de números de caras
            if n_caras != vg_dparametros[dtipo][3]: self._n_caras = vg_dparametros[dtipo][3]

            

         

        # Validación para el caso en el que si 

        # Estableciendo parámetros para la creación según el tipo de dato

            

        self.coord = self._gCoord(rango=rango)      # Coordenadas iniciales
        self._valores_caras_sec, self.valores_cara = self._gValores(forma=forma)    # Valores de las caras
        
        # Modificar los métodos traídos del padre
        self.unPaso = self._unPasoDado(self.unPaso)     # unPaso()

        # actualizamos los demás atributos
        self._aAtributos()

    def _gValores(self,
                  *inter_v: Tuple,                          # intervalo de valores
                  n_caras: int = None,                      # número de caras con valores
                  posic_sec: Tuple = None,                  # Posiciones de los valores en secuencia
                  dim: Tuple[int, int] = None,              # Dimensiones de la pieza
                  forma: formas_dado = None,                # Formas predeterminadas
                  ) -> tuple:            
        """"""

        # Caso 1: cuando forma toma un valor básico


        # > Validación de parámetros
        # Caso: no se especifica una forma y se deben pasar todos los demás argumentos
        if forma == None and any(not e for e in (n_caras, inter_v, posic_sec, dim)):
            lista = ['n_caras', 'inter_v', 'posic_sec', 'dim']
            lista = tuple([ e for e in lista if locals()[e] == None ])
            if len(lista) == 1: return f"!ERROR! Falta el argumento: {lista[0]}"
            else: return f"!ERROR! Faltan los argumentos: {lista}"
        
        # Caso: validando la colocación de los valores :-> posic_sec
        # Validación de contenido
        for e in posic_sec:
            if e != 1 and e != 0: return "!ERROR! Los valores de 'posic_sec' deben ser solo 0s o 1s."
        # Validación de cantidad de elementos
        posic_sec_unos = [ e for e in posic_sec if e == 1]      # todos los unos de 'posic_sec'
        if len(posic_sec_unos) < n_caras :
            return f"!ERROR! El número de caras ({n_caras}) es mayor que el número de posic_sec ({len(posic_sec_unos)})."
        elif len(posic_sec_unos) > n_caras :
            return f"!ERROR! El número de caras ({n_caras}) es mayor que el número de posic_sec ({len(posic_sec_unos)})."  

        # Caso: validación de la dimension :-> dim
        # Validación de cantidad
        if len(dim) != 2: return "!ERROR! La dimensión debe ser una tupla de tamaño 2."
        if dim[0]*dim[1] < n_caras: return "!ERROR! La dimensión no puede ser menor que el número de caras."
        # Validacion de la dimensión con respecto a la posición de los valores
        if len(posic_sec_unos) > dim[0]*dim[1]: return "!ERROR! La dimensión no puede ser menor que la posición de valores asignados."

        # Caso: validación de los intervalos de valores 'inter_v' 
        # Validación de orden y cantidad de elementos:
        inter_v_tuple = []
        for e in inter_v:
            if type(e) == tuple and len(e) == 2:
                if e[0] > e[1]: return "!ERROR! Los intervalos para 'iter_v' deben ser ordenados de mayor a menor."
            elif type(e) == tuple:
                if len(e) != 2: return "!ERROR! El tamaño de los intervalos  para 'iter_v' debe ser igual a 2."
            elif type(e) != tuple and type(e) != int:
                return "!ERROR! Los valores para inter_v solo pueden ser 'int' o 'tuple' de tamaño 2."
        
        # Validación según el número de cara, se aprovecha para crear la secuencia de valores
        sec_valores = []
        t_inter_v = list(inter_v)
        while len(t_inter_v) != 0:
            t_1 = choice(t_inter_v)             # Seleccionamos un elemento al asar
            t_inter_v.remove(t_1)               # quitamos dicho elementos de la lista
            if type(t_1) == int:
                if t_1 not in sec_valores: sec_valores.append(t_1)
            elif t_1[1] - t_1[0] == 1:
                t_2 = choice(t_1)
                if t_2 not in sec_valores: sec_valores.append(t_2)
                t_1 = list(t_1).remove(t_2)
                if t_2 not in sec_valores: sec_valores.append(t_1[0])
            else:
                t_2 = [ x for x in range(t_1[0], t_1[1] + 1) ]
                while len(t_2) != 0:
                    t_3 = choice(t_2)
                    t_2.remove(t_3)
                    if t_3 not in sec_valores: sec_valores.append(t_3)
        # Conclusión
        if len(sec_valores) < n_caras: 
            return f"!ERROR! El número de caras ({n_caras}) es mayor que el número de valores por cara ({len(sec_valores)})."
        elif len(sec_valores) > n_caras: 
            return f"!ERROR! El número de caras ({n_caras}) es menor que el número de valores por cara ({len(sec_valores)})."
        
        print(inter_v, posic_sec, dim, n_caras, sec_valores)

        # > Construcción de la matriz de valores
        p_sec_valores = 0
        p_posic_sec = 0
        matrix_valores = []
        for f in range(0, dim[0]):
            fila_temporal = []
            for c in range(0, dim[1]):
                if posic_sec[p_posic_sec] == 1:
                    fila_temporal.append(sec_valores[p_sec_valores])
                    p_sec_valores += 1
                else:
                    fila_temporal.append(0)
                p_posic_sec += 1
            matrix_valores.append(fila_temporal)

        return matrix_valores, sec_valores

    def _aAtributos(self) -> None:      # Actualizador de atributos
        # Actual. self._estado
        # Actual. self.cantidad_caras
        # Actual. cond_captura
        pass

    # Decorador del método unPaso()
    def _unPasoDado(self, funcion: Callable):
        def funcionDecorada():
            print()
            resutlado = funcion()
            print('Ahora hago esto')
            return resutlado
        return funcionDecorada


    

if __name__ == "__main__":
    """
    El resultado fila:

    <Caso 1> - Dado Básico
    pieza1 = Dado() -> un dado de la forma f1, f2 , f3

    <caso 2> - Dado Básico
    pieza2 = Dado((2,5), 9) -> un dado de la forma f1, pero con los valores de las caras [2-5, 9]

    <caso 3> - Dado Esp.
    pieza3 = Dado(posic_sec=(0,0,1,0,1,1,1,0,1)) -> modificar la posición (f1*)

    <caso 4> - Dado Esp.
    pieza4 = Dado(n_caras=4) -> seleccionar un numero de caras diferente al tipo (f1*)

    <caso 4.1> - Dado Esp.
    pieza41 = Dado(n_caras=5) -> la posición viene elegida en manera aleatoria (f1*)
    """

