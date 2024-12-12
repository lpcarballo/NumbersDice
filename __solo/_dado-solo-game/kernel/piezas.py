"""Piezas Moviles\n
Contiene todas las piezas móviles del juego
"""

from typing import Literal, Tuple, Callable
from random import sample, randint, choice

# Tipos de datos
list_dtipo = Literal['f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp']           # Tipos de dados según su forma
list_dir_mv = Literal['u', 'd', 'r', 'l']                                  # Dirección del movimiento
tipo_dim = Tuple[int, int]
list_atr = Literal['dtipo', 'n_caras', 'inter_v', 'dim', 'posic_sec']

# Variables globales
vg_dtipo = ('f1','f2', 'f3', 'f1*', 'f2*', 'f3*', 'fp')
vg_dtipo_b = ('f1','f2', 'f3')
vg_dtipo_e = ('f1*', 'f2*', 'f3*')
vg_dparametros = {        # tipo de dado <-> parámetros para la creación
    'f1': ((1,5), (3,3), (0,1,0,1,1,1,0,1,0), 5),
    'f2': ((1,6), (4,3), (0,1,0,1,1,1,0,1,0,0,1,0), 6),
    'f3': ((1,6), (3,4), (0,1,0,0,1,1,1,1,0,1,0,0), 6),
    'f1*': (3,3),
    'f2*': (4,3),
    'f3*': (3,4)
}
vg_atr = ('dtipo', 'n_caras', 'inter_v', 'dim', 'posic_sec')


class _PiezaMovil:
    """Clase abstracta\n
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
               dir_mv: list_dir_mv = 'd'):
        print("Solo hago esto.")


class Dado(_PiezaMovil):
    """Pieza-móvil Dado"""

    def __init__(self,
            dtipo: list_dtipo = None,
            inter_v: int | Tuple[int,int] = None,
            dim: Tuple[int,int] = None,
            posic_sec: Tuple = None,
            n_caras: int = None
        ) -> None:
        """"""

        self._dim = dim
        self._dtipo = dtipo
        self._inter_v = inter_v
        self._n_caras = n_caras       
        self._posic_sec = posic_sec

        self.sec_valores = []
        self._matrix_valores = []
       
        # Modificar los métodos traídos del padre
        self.unPaso = self._unPasoDado(self.unPaso)     # unPaso()

    def cond_iniciales():
        """Condiciones iniciales del dado"""
        pass

    def _gen_atributos(self,
                       atr: list_atr,           
                       ):
        match atr:
            case 'n_caras':
                pass
            case 'inter_v':
                pass
            case 'dim':
                pass
            case 'posic_sec':
                pass
            case 'dtipo':
                pass
    
    # (!) Esta función se borrará
    def __gen_atributos(self,
                  *inter_v: Tuple,                          # intervalo de valores
                  n_caras: int = None,                      # número de caras con valores
                  posic_sec: Tuple = None,                  # Posiciones de los valores en secuencia
                  dim: Tuple[int, int] = None,              # Dimensiones de la pieza
                  forma: list_dtipo = None,                 # Formas predeterminadas
                  ) -> tuple:            
        """Generador de atributos\n
        Se encarga de generar los valores de los atributos cuando
        estos no son pasados, y se dejan a disposición
        del programa.
        """

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

    def _act_atributos(self) -> None:      # Actualizador de atributos
        """Actualizador de atributos\n
        Muchas veces cuando se modifican valores dentro del dado,
        estos cambios implican cambios dentro de otros valores.
        Esta función se encarga de realizar estos cambios."""
        # Actual. self._estado
        # Actual. self.cantidad_caras
        # Actual. cond_captura
        
        pass

    # Decorador del método unPaso()
    def _unPasoDado(self, funcion: Callable):
        """Decorador de un un_paso() del padre
        Modifica el método del padre, ya que el movimiento es el padre
        es más simple y este tiene detalles particulares del dado.
        """
        def funcionDecorada():
            print()
            resutlado = funcion()
            print('Ahora hago esto')
            return resutlado
        return funcionDecorada


def dado(
    dtipo: list_dtipo = None,
    n_caras: int = None,
    inter_v: Tuple[int | Tuple[int,int]] = None,
    dim: Tuple[int,int] = None,
    posic_sec: Tuple = None,
) -> str | Dado:
    """Constructor de la clase Dado\n
    Para utilizar el objeto Dado, se aconseja utilizar
    esta función, ya que tiene validaciones y configuraciones
    específicas.
    """

    cond = any((dtipo != None, n_caras != None, inter_v != None, dim != None, posic_sec != None))
    
    # Si se paso algún argumento
    if cond:

        # validación de la dimension :: dim
        if dim != None:
            if type(dim) != tuple:
                return "'dim' tiene que ser una tupla"
            elif len(dim) != 2: return "'dim' tiene que ser una tupla de tamaño dos."
            if type(dim[0]) != int or type(dim[1]) != int: return "Los elementos de 'dim' tiene que ser enteros."
            # Validación lógica
            if dim[0] < 3 or dim[1] < 3: return "'dim' no puede ser menor de (3,3)"
        
        # Validación de posición en secuencia :: posic_sec
        if n_caras != None: j = 0   # Este valor ayuda a validar 'n_caras' con respecto a 'posic_sec'
        if posic_sec != None:
            # validación de forma
            if type(posic_sec) != tuple: return "'posic_sec' tiene que ser una tupla."
            else:
                # validación con respecto a 'dim'
                if dim != None and len(posic_sec) != dim[0]*dim[1]:
                    return f"'posic_sec' tiene que ser una tupla de tamaño {dim[0]*dim[1]}."
                for i in posic_sec:
                    if i != 1 and i != 0: return "Los elementos de 'posic_sec' tienen que ser solo 0s o 1s."
                    if n_caras != None: j += i
            # validación lógica
            if len(posic_sec) < 9: return "'posic_sec' no puede ser menor de 5."

        # Validación del número de caras :: n_caras
        if n_caras != None:
            # validación de forma:
            if type(n_caras) != int: return "'n_caras' debe ser un entero."
            # Validación con respecto a 'posic_sec'
            if posic_sec != None and j != n_caras:
                return "El valor del número de caras tiene que coincidir con la cantidad de 1 en posic_sec."
            # validación con respecto a dim
            if dim != None and n_caras > dim[0]*dim[1]: return "n_caras no puede ser mayor a la dimensión."
            # validación lógica
            if n_caras < 5: return "'n_caras' no puede ser menor de 5."
        
        # Validación de intervalo de valores :: inter_v
        if inter_v != None:
            if type(inter_v) != tuple: return "'inter_v' tiene que ser una tupla."
            else:
                for i in inter_v:
                    if type(i) != int | tuple: return "Los elementos de 'inter_v' tienen que ser números o tuplas."
                    else:
                        if type(i) == tuple and len(i) != 2: return "Las tuplas internas de 'inter_v' tiene que ser de tamaño 2"
            # validación lógica
            # ... por definir ...

        # Validación del tipo de dado :: dtipo
        if dtipo in vg_dtipo:
            if dtipo in vg_dtipo_b:
                n_caras     = vg_dparametros[dtipo][3]
                inter_v     = vg_dparametros[dtipo][0]
                dim         = vg_dparametros[dtipo][1]
                posic_sec   = vg_dparametros[dtipo][2]
            elif dtipo in vg_dtipo_e:
                dim         = vg_dparametros[dtipo]
        elif dtipo != None:
            return f"'dtipo' solo permite estos valores: {vg_dtipo}"

    # No se pasó ningún argumento
    else:
        dtipo       = 'f1'
        n_caras     = vg_dparametros[dtipo][3]
        inter_v     = vg_dparametros[dtipo][0]
        dim         = vg_dparametros[dtipo][1]
        posic_sec   = vg_dparametros[dtipo][2]

    return Dado(
        dtipo,
        n_caras,
        inter_v,
        dim,
        posic_sec,
    )

if __name__ == "__main__":
    """
    El resultado fila:

    <Caso 1> - Dado Básico [x]
    pieza1 = Dado() -> un dado de la forma f1

    <Caso 1.1> - [x]
    comprobar para los demás valores básicos y especiales

    <Caso 2> - validación de la dimensión [x]

    <Caso 3> - Validación del número de caras [x]

    <Caso 4> - Validación de la posición en secuencia [x]

    <Caso 5> - Validaciones lógicas []
    dim no puede ser menor de 3                     [x]
    posic_sec no puede tener menos de 9 elementos   [x]
    n_caras no puede ser menor de 5                 [x]
    inter_v no puede tener menos de 5 elementos     []

    <caso 2> - Dado Básico []
    pieza2 = Dado((2,5), 9) -> un dado de la forma f1, pero con los valores de las caras [2-5, 9]

    <caso 3> - Dado Esp.
    pieza3 = Dado(posic_sec=(0,0,1,0,1,1,1,0,1)) -> modificar la posición (f1*)

    <caso 4> - Dado Esp.
    pieza4 = Dado(n_caras=4) -> seleccionar un numero de caras diferente al tipo (f1*)

    <caso 4.1> - Dado Esp.
    pieza41 = Dado(n_caras=5) -> la posición viene elegida en manera aleatoria (f1*)
    """

    # Función para mostrar los valores de los atributos
    def print_atributos(objeto, list_atributos):
        for a in list_atributos:
            if hasattr(objeto, a):
                if a != '_dim': print(a, ":\t", getattr(objeto, a))
                else: print(a, ":\t\t", getattr(objeto, a))
            else:
                print(objeto)
                break
        print()
            
    
    atributos = ('_dtipo', '_n_caras', '_inter_v', '_dim', '_posic_sec')
    
    pieza1 = dado(posic_sec=(0,1))
    print_atributos(pieza1, atributos)

