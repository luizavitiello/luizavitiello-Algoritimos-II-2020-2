# -*- coding: utf-8 -*-

                                  
class Pessoa:
         def  __init_(self):
             self.nome=None 
             self._codigo=None
             self.endereco=None
             self.telefone=None

         def setNome(self,nome):
             self.nome=nome

         def setCodigo(self,codigo):
             self._codigo=codigo

         def getNome(self):
             return self.nome

         def getCodigo(self):
             return self._codigo

         def setEndereco(self,endereco):
             self.endereco=endereco

         def setTelefone(self,telefone):
             logado=True
             if logado:
                 self.__telefone=telefone

         def getEndereco(self):
             return self.endereco

         def getTelefone(self):
             logado=True
             if logado:
                 return self.__telefone        
             
         def imprimir(self):
             print("Nome:  ",self.getNome())
             print("Telefone: ",self.getTelefone())


         def obterdados(self):
            self.setNome(str(input("Qual nome? ")))
            self.setTelefone(input("Qual telefone? "))
            self.setEndereco(input("Qual endereco? "))
            self.setCodigo(int(input("Qual codigo? ")))

#########################################################################
class Fisica:
    def __init__(self):
        self.__cpf=None
        self._idade=None
        self.peso=None
        self.altura=None


    def getCpf(self):
        logado=True
        if logado:
            return self.__cpf

    def getIdade(self):
         return self.idade
    def getPeso(self):
         return self.idade

    def getAltura(self):
         return self.altura

    def setCpf(self,cpf):
        logado=True
        if logado:
            self.__cpf=cpf
    
    def setIdade(self,idade):
         self.idade=idade

    def setPeso(self,peso):
         self.peso=peso

    def setAltura(self,altura):
         self.altura=altura       

    def dados(self):
        self.setCpf(int(input("Qual cpf? ")))
        self.setIdade(int(input("Qual idade? ")))
        self.setPeso(float(input("Qual peso? ")))
        self.setAltura(float(input("Qual altura? ")))
        imc=self.getPeso()/self.getAltura()**2
        print("Seu peso ideal é: ",imc)
        
    def mostraCPF(self):
        print("CPF:  ",self.getCpf())

class Juridica:
    def __init__(self):
        self.__cnpj=None
        self.__inscricaoEstadual=None
        self.qtdFuncionarios=None

    def getCNPJ(self):
        logado=True
        if logado:
            return self.__cnpj
    def setCNPJ(self,cnpj):
        logado=True
        if logado:
            self.__cnpj = cnpj

    def getincricaoEstadual(self):
        logado=True
        if logado:
            return self.__inscricaoEstadual
    def setinscricaoEstadual(self,inscricaoEstadual):
        logado=True
        if logado:
            self.__inscricaoEstadual = inscricaoEstadual
    def getFuncionario(self):
        return self.qtdFuncionarios

    def setFuncionario(self,qtdFuncionarios):
        self.qtdFuncionarios = qtdFuncionarios

    def cadastroempresa(self):
        self.setCNPJ(int(input("Qual CNPJ? ")))
        self.setinscricaoEstadual(input("Qual registro da empresa? "))
        self.setFuncionario(int(input("Qual a quantidade de funcionários? ")))
        print("Empresa Cadastrada com Sucesso")      

    def imprimeCNPJ(self):
        print("CNPJ: ",self.getCNPJ())


    def notafiscal(self):
        print("Nota Fiscal")
        print("CNPJ: ",self.getCNPJ())
        print("Inscrição Estadual: ",self.getincricaoEstadual())
        print("Quantidade Funcionários: ",self.getFuncionario())
    
        
         
        
#####################################################################        
menu=[0,1,2,3,4,5,6,7]
p = Pessoa()
f=Fisica()
j=Juridica()
def validamenu():
          print(""" Menu de Navegação:
                      0-  Sair
                      1- Cadastro
                      2- Mostrar Nome e Telefone
                      3- Calcular IMC
                      4- Mostrar CPF
                      5- Cadastrar empresa 
                      6- Mostrar CNPJ
                      7- Emitir Nota Fiscal
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
                  

#############Programa Principal##################          
while True:
         escolha=validamenu()
         if escolha==0:
                  print("Encerrando programa...")
                  break
         elif escolha==1:
             p.obterdados()
         elif escolha==2:
             p.imprimir()
         elif escolha==3:
             f.dados()
         elif escolha==4:
             f.mostraCPF()
         elif escolha==5:
             j.cadastroempresa()
         elif escolha==6:
             j.imprimeCNPJ()

         elif escolha==7:
             j.notafiscal()
