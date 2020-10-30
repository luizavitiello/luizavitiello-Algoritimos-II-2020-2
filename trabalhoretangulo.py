# -*- coding: utf-8 -*-
'''Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura e largura.

A classe deve ter os seguintes métodos:

     Método construtor

     Método que calcula a área do retângulo ( altura * largura) e retorna o resultado

     Método que imprime os valores dos atributos da classe.'''

                                  
class Retangulo:
         def  __init_(self):
             self.largura=None 
             self.altura=None  

         def setLargura(self,largura):
             self.largura=largura

         def setAltura(self,altura):
             self.altura=altura

         def getLargura(self):
             return self.largura

         def getAltura(self):
             return self.altura
         
         def imprimir(self):
             print("Altura:  ",self.getAltura())
             print("Largura: ",self.getLargura())
             resultado = (self.getLargura()*self.getAltura())
             print("A área do retângulo é: ",resultado)

         def calcular(self):
             print("Calcule a área do retangulo",)
             self.setAltura(float(input("Qual a altura do retangulo? ")))
             self.setLargura(float(input("Qual a largura do retangulo? ")))
             resultado=(self.getLargura()*self.getAltura())
             print(" A área do retangulo é:",resultado)

         
menu=[0,1,2,3]
r = Retangulo()
def validamenu():
          print(""" Menu de Navegação:
                      0-  Sair
                      1- Calcular
                      2-  Imprimir
                      """)
          escolha=input('Escolha:')
          try:
                  escolha = int(escolha)
                  if escolha in menu:
                     return escolha
                  else:
                     print('Opção inexistente. tente novamente')
          except:
                  print("Parâmetro inválido, tente novamente.")
                  

 ############Programa Principal##################          
while True:
         escolha=validamenu()
         if escolha==0:
                  print("Encerrando programa...")
                  break
         elif escolha==1:
             r.calcular()
         elif escolha==2:
             r.imprimir()
