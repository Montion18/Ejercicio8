from Classconjunto import Conjunto
from Manejador import manejador

def op0():
    print("Presione enter para salir\n")
def op1():
    print("Union de dos conjuntos\n")
    a=int(input("Ingrese un numero de conjunto "))
    b=int(input("Ingrese otro numero de conjunto "))
    a-=1
    b-=1
    f=conj1.union(a,b)
    f.mostrar()
def op2():
    print("Diferencia de dos conjuntos\n")
    a=int(input("Ingrese un numero de conjunto "))
    b=int(input("Ingrese otro numero de conjunto "))
    a-=1
    b-=1 
    f=conj1.dif(a,b)
    f.mostrar()
    
def op3():
    print("Igualdad de conjuntos\n")
    a=int(input("Ingrese un numero de conjunto "))
    b=int(input("Ingrese otro numero de conjunto "))
    a-=1
    b-=1
    
    f=conj1.igualdad(a,b)
    if f ==True:
        print("Los conjuntos ingresados son iguales")
    else: print("Los conjuntos son distintos")



switcher={
    0:op0,
    1:op1,
    2:op2,
    3:op3
    }

def switch(op):
    func = switcher.get(op, lambda: print("Opción incorrecta\n"))
    func()


if __name__=='__main__':
    bandera=False
    conj1=manejador()
    conj1.Crearlista()
    
    while not bandera:
        print("---MENU---")
        print("1.Union\n")
        print("2.Diferencia\n")
        print("3.Verifica igualdad\n")
        op=int(input("Seleccione una opcion \n"))
        switch(op)
        bandera=int(op)==0

