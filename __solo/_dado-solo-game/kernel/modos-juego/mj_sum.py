"""Modo de Juego - Sum
Este modulo se encarga de crear/controlar/gestionar la información de un partido en
modalidad 'sum'. Ya el objeto partido contiene en su interior todos los métodos que
llevan acabo las tres acciones anteriores.

EJEMPLO
-------
partido1 = Partido(
        modo: variantes_sum,
        tablero: Tablero,
        pieza: Dado
    )   # creamos una instancia de un partido sum

partido1.iniciar()          # Inicia un partido de NumbersDice
print(partido1.resumen)     # Muestra toda la información final del partido

"""

from typing import Literal
from random import randint

import piezas as piezas, tablero
from piezas import Dado
from tablero import Tablero

variantes_sum = Literal['uniforme', 'normal']
tipos_movimientos = Literal['u', 'd', 'r', 'l']

class Partido:
    """"""

    coords = []            # coordenadas de las piezas
    pjugador = [0]         # Puntos por jugador
    resumen = None         # contiene toda la información del partido

    def __init__(self,
                 modo: variantes_sum = 'uniforme',
                 tablero: Tablero = None,
                 pieza: Dado = None
                 ) -> None:
        """"""
        # Instanciando la el dado
        if pieza == None: 
            self.p = Dado()
        
        
        
        
        self.t = [tablero]      # tableros

    def _coordIniciales(self) -> None:
        self.coords.append(self.p.coord)

    def _condCaptura(self,
                     vp: int,       # Valor de la pieza para la condición de captura
                     vt: int,       # Valor del tablero
                     coord: tuple
                     ) -> None:
        if vp == vt:
            self.pjugador[0] = self.t[0].valores_casillas[coord[0]][coord[1]]
            self.t[0].valores_casillas[coord[0]][coord[1]] = 0

    def moverDado(self,
                  movimiento: tipos_movimientos):
        match movimiento:
            case 'u':
                self.coords[0] = (self.coords[0][0] - 1, self.coords[0][1])
                print(self.coords[0])
                self._condCaptura(self.p[0].valores_cara[1][1],
                                  self.t[0].valores_casillas[self.coords[0][0]][self.coords[0][1]],
                                  self.coords[0])
            case 'd':
                self.coords[0] = (self.coords[0][0] + 1, self.coords[0][1])
            case 'r':
                self.coords[0] = (self.coords[0][0], self.coords[0][1] + 1)
            case 'l':
                self.coords[0] = (self.coords[0][0], self.coords[0][1] - 1)
            case _:
                return "ERROR: Valor de movimiento no valido"

    def iniciar():
        pass



if __name__ == '__main__':    
    partido1 = Partido()
