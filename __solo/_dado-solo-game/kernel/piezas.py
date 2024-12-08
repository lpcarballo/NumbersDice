"""Contiene todas las piezas móviles del juego"""

from typing import Literal, Tuple

import _importaciones as _imp
from random import sample, randint, choice

class _PiezaMovil:
    """Clase abstracta
    Contiene toda la información común de las piezas móviles.
    """

    _estado: str = None
    coord: tuple[int,int] = None
    cantidad_caras: int = None
    cond_captura: int = None

    def _gCoord(self, 
                rango: int | tuple[int, int]
                ) -> tuple[int, int]:   # Generador de coordenadas
        if type(rango) == int:
            return _imp.randint(1,rango), _imp.randint(rango)
        elif type(rango) == tuple and len(rango) == 2:
            return _imp.randint(rango[0], rango[1]), _imp.randint(rango[0], rango[1])
    
    def unPaso(self, 
               dir_mv: _imp.dir_mv = 'd'):
        print("Solo hago esto.")


class Dado(_PiezaMovil):
    """"""

    f_dado: _imp.f_dado = 'f1'                              # Forma del dado
    r_valores = _imp.fd_rvalor[f_dado][2]                   # Rango de valores de las caras

    def _gValores(self,
                  *inter_v: Tuple,                          # intervalo de valores
                  n_caras: int = None,                      # número de caras con valores
                  posic_sec: Tuple = None,                  # Posiciones de los valores en secuencia
                  dim: Tuple[int, int] = None,              # Dimensiones de la pieza
                  forma: _imp.f_dado = None,                # Formas predeterminadas
                  ) -> tuple:             
        """"""

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
    def _unPasoDado(self, funcion: _imp.Callable):
        def funcionDecorada():
            print()
            resutlado = funcion()
            print('Ahora hago esto')
            return resutlado
        return funcionDecorada

    """
    def __init__(self,
            forma: _imp.f_dado = 'f1',
            rango: int | tuple[int, int] = None
        ) -> None:
        """"""

        # Definiendo el rango de valores según la forma del dado
        # ya que no fue pasado ningún rango
        if rango == None:
            match forma:
                case 'f1': rango = (1,5)
                case 'f2': rango = (1,6)
                case _: return "ERROR: Valor de forma no valido."
            

        self.coord = self._gCoord(rango=rango)      # Coordenadas iniciales
        self._valores_caras_sec, self.valores_cara = self._gValores(forma=forma)    # Valores de las caras
        
        # Modificar los métodos traídos del padre
        self.unPaso = self._unPasoDado(self.unPaso)     # unPaso()

        # actualizamos los demás atributos
        self._aAtributos()
        """
    

if __name__ == "__main__":
    """
    dado1 = Dado('f2')
    print("\nValores de las Caras: ")
    for i in dado1.valores_cara: print(i)
    print("Valores de las caras en secuencia: ", dado1._valores_caras_sec)
    print("Condición de captura: ", dado1.cond_captura)
    print()
    

    pieza1 = _PiezaMovil()
    pieza1.unPaso(dir_mv='d')

    dado1 = Dado((1,6))
    dado1.unPaso(dir_mv='d')
    """

