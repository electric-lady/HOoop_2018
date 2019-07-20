#!/usr/bin/python

#-*-coding:utf-8 -*-

import random


class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila = 0
        self.fila = []


class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila += 1    #es equivalente a self.enfila = self.enfila +1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        self.enfila-=1  #siempre que atienden al cliente disminuye en 1 el tamaño de la fila
        self.fila.pop(0) #saca el pimer elemento de la fila
    
    def abrircajanueva(self, maxenfila, filanueva):
        """Separo en 2 la FilaPreferencial según tenga una cantidad par o 
        impar de elementos, para referirime al objeto uso self y para
         manipular alguno de sus atributos es self.atributo 
        self.filanueva = [] esta lìnea no va porque filanueva es una Fila
         y ya heredó"""
        if((self.enfila % 2 ) == 0):
            filanueva = self.fila[int(0.5*self.enfila): self.enfila+1]
            self.fila = self.fila[0:int(0.5* self.enfila) + 1]
        else:
            filanueva = self.fila[int(0.5 * (self.enfila + 1)): self.enfila + 1 ]
            self.fila = self.fila[0:int(0.5 * (self.enfila + 1 ))]
        
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila += 1  #siempre que llega un cliente aumenta en 1 el tamaño de la fila
        self.fila.append(cliente)


    def atender(self):
        """Atiende al proximo cliente preferencial"""
        self.enfila-=1
        self.fila.pop(0)    

    
class Cliente(object):
    """clase cliente """
    def __init__(self, dni):
        """ constructor de la clase cliente """
        self.dni = dni
        self.categoria = None

    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria = categoria
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    '''Creo un objeto de la categoría FilaPreferencial y otro objeto de la categoría 
    FilaGeneral con () vacío pues no tienen parámetros externos'''
    maxenfila = 3
    fila_general = FilaGeneral()
    fila_preferencial_1 = FilaPreferencial()

    """Creo una lista aleatoria de clientes,si es múltiplo de 5
     lo considero preferencial, llamando al método modificarcategoria
      le cambio la categoria y llamando al métotdo insertar lo agrego a
      la FilaPreferencial. Si no es múltiplo de 5 va a la fila general"""
    """A cada fila le asigno los objetos: 'clientes', que cumplan cierta condición"""

    for i in range (0, 60):
        dni = random.randint(1, 61)
        cliente = Cliente(dni)
        print("$$$$$$$$$$", fila_preferencial_1.enfila)
        print("oooooooooo", i)

        if (dni % 5 == 0):
            cliente.modificarcategoria("Preferencial")
            #print(type(cliente))
            fila_preferencial_1.insertar(cliente)
            """if (fila_preferencial_1.enfila > maxenfila):
                fila_injusta = FilaPreferencial()
                #print("SSSSSSSSSSSSSSSSSSSSSSSS", fila_injusta)
                filanueva = fila_preferencial_1.abrircajanueva(maxenfila, fila_injusta.fila)"""
        else:
            #print(type(cliente))
            fila_general.insertar(cliente)

    i = 0
    while (i < fila_general.enfila):
        print(fila_general.fila[i].dni, fila_general.fila[i].categoria)
        i += 1

    i = 0
    while (i < fila_preferencial_1.enfila):
        print("indice:", i)
        print("len()", len(fila_preferencial_1.fila))
        print("$$$$$$$$$$", fila_preferencial_1.enfila)

        print(fila_preferencial_1.fila[i].dni, fila_preferencial_1.fila[i].categoria)
        i += 1

    """i = 0
    while (i < fila_injusta.enfila):
        print(fila_injusta.fila[i].dni, fila_injusta.fila[i].categoria)
        i += 1"""


    """Defino un máximo de clientes posibles en la fila_preferencial_1 y creo el objeto
     fila_injusta(filanueva dentro del método abircajanueva) de la clase FilaPreferencial
    para llamar al método abrircajanueva que separa la fina original en 2 partes de modo
     que quien está en la mitad de la fila es atendido antes que el segundo , por eso es injusta"""

        
