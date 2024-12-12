"""Contiene el objeto Tablero"""

import _importaciones as _imp

class Tablero:
    """Objeto mediante el cual se construyen todos los tableros del juego"""
    
    def _generadorValores(self) -> _imp.Tuple[int, int]:
        """Genera los valores de la caras del tablero"""
        valores = [ _imp.randint(1,5) for x in range(36) ]
        tablero = [ valores[0 + i*6 : 6 + i*6 ] for i in range(6)]
        return valores, tablero

    def __init__(self) -> None:
        valores = self._generadorValores()
        self.cantidad_casillas = 36
        self.valores_casillas = valores[1]
        self._valores_casillas_sec = valores[0]

if __name__ == '__main__':
    tablero1 = Tablero()
    for i in tablero1.valores_casillas:
        print(i)
    print(tablero1._valores_casillas_sec)
