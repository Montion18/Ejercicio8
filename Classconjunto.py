import csv
class Conjunto:
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
        
    def crear(self,list):
        for i in range(len(list)):
            list[i]=int(list[i])
            self.__lista=list

    def mostrar(self):
        print(self.__lista)
    def __add__(self,otro):
        self.__lista.sort()
        otro.__lista.sort()
        listan=Conjunto()
        for i in self.__lista:
            if i not in listan.__lista:
                listan.__lista.append(i)
        for i in otro.__lista:
            if i not in listan.__lista:
                listan.__lista.append(i)
        return listan
    def __sub__(self,otro):
        self.__lista.sort()
        otro.__lista.sort()
        listan=Conjunto()
        for i in self.__lista:
            if i not in listan.__lista:
                if i not in otro.__lista:
                    listan.__lista.append(i)
        return listan

    def __eq__(self,otro):
        self.__lista.sort()
        otro.__lista.sort()
        l=False
        if len(self.__lista)==len(otro.__lista):
            for i in self.__lista:
                if i in self.__lista and i in otro.__lista:
                    l=True
                else:
                    l=False
                    return l
        
        return l
    
   
        
        



    