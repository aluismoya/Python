
def suma(val1,val2,val3):
    return val1+val2+val3

resultado = suma(10,20,30)
print(resultado)

def suma2(parametro_requerido,*args):
    total = 0
    print(parametro_requerido)
    for valor in args:
        total+=valor
    return total

resultado = suma("Este es un argumento requerido", 10,20,30,40,50,60)
print(resultado)

def suma3(parametro_requerido,*args):
    
def usuarios_requeridos(**kwargs):
    print(kwargs)

resultado = suma("ESte es un argumento requerido", 10,20,30,40,50,60)
print(resultado)

usuarios_requeridos(codi=True, facilito=False)


def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido",10, 20, valor_uno=True, valor_dos=False)