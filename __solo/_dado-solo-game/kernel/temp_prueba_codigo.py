import piezas

pieza1 = piezas.Dado()

valor = pieza1._gValores(
    (1,13),
    n_caras=13,
    posic_sec=(0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0),
    dim=(5,5)
)
if type(valor) == tuple:
    print()
    for f in valor[0]:
        print(f)
    print()

