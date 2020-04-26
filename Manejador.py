from Classconjunto import Conjunto
import csv
class manejador:
    __lista=[]
    def Crearlista(self):
        archivo=open("conjuntos.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            conj1=Conjunto()
            conj1.crear(fila)
            self.__lista.append(conj1)
            
    def mostrar(self):
        print(self.__lista[0].mostrar())

    def union(self,a,b):
        return self.__lista[a]+self.__lista[b]
    def dif(self,a,b):
        return self.__lista[a]-self.__lista[b]
    def igualdad(self,a,b):
        return self.__lista[a]==self.__lista[b]
        
       
    
            