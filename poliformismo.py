class Veiculo:
    def __init__(self):
        self.marca=None
        self.qtdsRodas=None
        self.modelo=modelo=None
        self.velocidade=None
        self.velocidadesomada=None
        self.freavel=None

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca


    def getquantidadeRodas(self):
        return self.qtdsRodas
    def setquantodadeRodas(self,qtdsRodas):
        self.qtdsRodas=qtdsRodas


    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo


    def getVelocidade(self):
        return self.velocidade
    def setVelocidade(self,velocidade):
        self.velocidade=velocidade

    
    def getVelocidadeSoma(self):
        return self.velocidadesomada
    def setVelocidadeSoma(self,velocidadesomada):
        self.velocidadesomada=velocidadesomada

    def getVelocidadeFrea(self):
        return self.freavel
    def setVelocidadeFrea(self,freavel):
        self.freavel=freavel
    
    def cadastraVeiculo(self):
        self.setMarca(input("Marca: "))
        self.setquantodadeRodas(input("Quantidade de rodas: "))
        self.setModelo(input("Qual o modelo: "))
        self.setVelocidade(input("Velocidade atual: "))

    def AceleraVeiculo(self):
        self.setVelocidadeSoma(int(input("Acelerar + ")))
        ac= int(self.getVelocidade()) + int(self.getVelocidadeSoma())
        print("Velocidade atualizada do carro: ",ac)

    def FrearVeiculo(self):
        self.setVelocidade(int(input("Frear - ")))
        ac= int(self.getVelocidade()) - int(self.getVelocidadeSoma())
        print("Velocidade atualizada do carro: ",ac)
        
    def mostraVeiculo(self):
        print("Marca: " +str(self.getMarca()))
        print("Quantidade Rodas: " ,self.getquantidadeRodas())
        print("Modelo: " +str(self.getModelo()))
        print("Velocidade Atual: " ,self.getVelocidade())
#################################################################
class Bicicleta(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.numMarchas=None
        self.bagageiro=None
        
    def getnumMarchas(self):
        return self.numMarchas
    def setNumMarchas(self,numMarchas):
        self.numMarchas=numMarchas


    def getBagageiro(self):
        return self.bagageiro
    def setBagageiro(self,bagageiro):
        self.bagageiro=bagageiro


    def cadastraBicicleta(self):
        Veiculo.cadastraVeiculo(self)
        self.setNumMarchas(int(input("Número de marchas: ")))
        self.setBagageiro(int(input("Bagageiro: ")))

    def mostraBicicleta(self):
        Veiculo.mostraVeiculo(self)       
        print("Número de Marchas: " ,self.getnumMarchas())
        print("Bagageiro: " ,self.getBagageiro())
################################################################
class Automovel(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.potenciaDoMotor=None

    def getPotencia(self):
        return self.potenciaDoMotor
    def setPotencia(self,potenciaDoMotor):
        self.potenciaDoMotor=potenciaDoMotor

    def cadastraAutomovel(self):
        Veiculo.cadastraVeiculo(self)
        self.setPotencia(int(input("Qual a potência? ")))
    def mostraAutomovel(self):
        Veiculo.mostraVeiculo(self)
        print("Potência do automóvel: " ,self.getPotencia())
###########################################################################
class Moto(Automovel):
    def __init__(self):
        Automovel.__init__(self)
        self.partidaeletrica=None

    def getPartida(self):
        return self.partidaeletrica
    def setPartida(self,partidaeletrica):
        self.partidaeletrica=partidaeletrica

    def CadastraMoto(self):
        Automovel.cadastraAutomovel(self)
        self.setPartida(float(input("Partida: ")))

    def mostraMoto(self):
        Automovel.mostraAutomovel(self)
        print("Partida: " ,self.getPartida())
#######################################################
class Carro(Automovel):
    def __init__(self):
        Automovel.__init__(self)
        self.qtdPortas=None

    def getPortas(self):
        return self.qtdPortas
    def setPortas(self,qtdPortas):
        self.qtdPortas=qtdPortas


    def cadastraCarro(self):
        Automovel.cadastraAutomovel(self)
        self.setPortas(int(input("Quantidade de portas: ")))

        
    def mostraCarrro(self):
        Automovel.mostraAutomovel(self)
        print("Número de Portas: " ,self.getPortas())


########Programa Principal####################

menu={0,1,2,3,4,5,6,7,8,9,10,11,12}
def validamenu():
          print(""" Menu de Navegação:
                      0-  Sair
                      1- Cadastro Veículo
                      2- Mostrar Informações do Veículo
                      3- Acelerar Veículo
                      4- Frear Veículo
                      5- Cadastrar Bicicleta
                      6- Mostrar informações bicileta
                      7-Cadastra automóvel
                      8-Mostra automóvel
                      9- Cadastrar Moto 
                      10- Mostrar informações moto
                      11- Cadastrar Carro
                      12- Mostrar informações carro
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
v=Veiculo()
b=Bicicleta()
a=Automovel()
m=Moto()
c=Carro()
while True:

         escolha=validamenu()
         if escolha==0:
                  print("Encerrando programa...")
                  break
         elif escolha ==1:
            v.cadastraVeiculo()
         elif escolha==2:
            v.mostraVeiculo()
         elif escolha==3:
             v.AceleraVeiculo()
         elif escolha==4:
             v.FrearVeiculo()
         elif escolha==5:
            b.cadastraBicicleta()
         elif escolha==6:
            b.mostraBicicleta()
         elif escolha==7:
            a.cadastraAutomovel()
         elif escolha==8:
             a.mostraAutomovel()
         elif escolha==9:
             m.CadastraMoto()
         elif escolha==10:
            m.mostraMoto()
         elif escolha==11:
            c.cadastraCarro()
         elif escolha==12:
             c.mostraCarrro()
            
        
      



    
