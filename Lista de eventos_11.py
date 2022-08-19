from re import S
from typing import List

#
# Clase Lista_de_eventos que nos permitira almacenar
# informacion acerca de los eventos
#

# Practicas de programacion de codigo legible

# ---------------------------------------------------------------
# 1.Camel Casel 
# Se toma la nomenclatura Camel Casel
# ---------------------------------------------------------------

# ------------------------------------------------
#2.Uso de verbos consistentes tanto en los metodos como en las funciones:  
## ------------------------------------------------
class ListaDeEventos:

    def __init__(self):
        self.size=0
        self.lista=[]
    
    def agregarEvento(self,nuevoIdEvento):
        self.lista.append(nuevoIdEvento)
        self.size+=1
    
    def mostrarEventos(self):
        for i in self.lista:
            print(i)


# ------------------------------------------------
#3.Modularizacion del codigo:  
# mediante la creacion de las siguientes funciones
## ------------------------------------------------



# ------------------------------------------------
#4.Las variables usadas  no tienen una letra a excepcion de aquellas que son para iterar:  
## ------------------------------------------------


# ------------------------------------------------
#5.Numero Magico: 
#Se toma un numero magico porque el llenado no 
# debe ser necesariamente  un numero especifico
## ------------------------------------------------
def llenarListaPrueba(listaObjeto):#Esta funcion nos permitira llenar un objeto Lista de eventos
                                      #Con una cantidad consecutiva de numeros 
    
    numeroDeIteraciones=input("Escriba cuantos numeros se insertaran: ") #->Numero magico
    
    for i in range(numeroDeIteraciones):
        listaObjeto.agregarEvento(i)



def introducirIdBuscado():#Esta funcion nos permitira hacer entradas de los
                # eventos a buscar , asi evitando repeticion
                # de fragmentos de codigo

    idEntero=input("Ingrese el id del evento: ")
    return idEntero

def buscarEvento(listaEventosEntradaIds,idEventoBuscado):

    for i in listaEventosEntradaIds:
        if(idEventoBuscado==i):
            return True

    return False

def mensaje(bolean_valor):

    if(bolean_valor):
        print("Encontrado")

    else:
        print("No encontrado")

# ------------------------------------------------
#6.Uso de sustantivos en objetos:  
## ------------------------------------------------
listaTest=ListaDeEventos()