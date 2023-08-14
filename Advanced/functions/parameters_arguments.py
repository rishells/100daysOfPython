# ARGS

def calcular_perimetro(*args):
    perimetro = 0

    for lado in args:
        perimetro += lado
    return perimetro


perimetro = calcular_perimetro(1,2,3)
print(perimetro)

# KWARGS

def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])


funcion_kwargs(name="Ricardo", apellido="Conchas")