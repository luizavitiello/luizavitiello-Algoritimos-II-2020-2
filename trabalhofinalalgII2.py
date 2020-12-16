menu=[0,1,2,3,4,5,6,7,8,9]

clientes=[]
livros=[]  
#####################################################################################
class Cliente:
    def __init__(self):
        self.nome=None
        self.__cod=None
        self.__cpf=None
        self.telefone=None
        self.endereco=None
   
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome=nome
    
    def getCod(self):
        logado=True
        if logado:
            return self.__cod
    def setCod(self,cod):
        logado=True
        if logado:
            self.__cod=cod
        
    def getCpf(self):
        logado=True
        if logado:
            return self.__cpf
    def setCpf(self,cpf):
        logado=True
        if logado:
           self.__cpf=cpf
            
    def getTel(self):
         return self.telefone
    def setTel(self,telefone):
         self.telefone=telefone

    def getEnd(self):
        return self.endereco
    def setEnd(self,endereco):
        self.endereco=endereco

    def cadastroCli(self):
        c=Cliente()
        c.setNome(input("Informe o nome do cliente: "))
        c.setCod(input("Informe o codigo do cliente: "))
        c.setCpf(input("Informe o cpf do cliente: "))
        c.setTel(input("Informe o telefone do cliente: "))
        c.setEnd(input("Informe o endereço do cliente: "))
        clientes.append(c)
        print("Cliente cadastrado com sucesso")

        
    def listarC(self):
        for c in clientes:
            print("Nome:",c.getNome(),"\nCódigo: ",c.getCod(),"\nCpf: ",c.getCod(),"\nTelefone: ",c.getTel(),"\nEndereço: ",c.getTel())
    


##########################################################################
class Livro:
    def __init__(self):
        self.nome=None
        self.__cod=None
        self.escritor=None
        self.estoque=None
    
    def getNome(self):
        return self.nome
    def setNome(self,nome): 
        self.nome=nome
    
    def getCod(self):
        logado=True
        if logado:            
            return self.__cod
    def setCod(self,cod):
        logado=True
        if logado:  
            self.__cod=cod
        
    def getEstoque(self):
        return self.estoque
    def setEstoque(self,estoque):
        self.estoque=estoque
    

    def getEscritor(self):
        return self.escritor
    def setEscritor(self,escritor):
        self.escritor=escritor

    
    def cadastro(self):
        l=Livro()
        l.setNome((input("Digite o nome do livro: ")))
        l.setCod((input("Digite o cod do livro: ")))
        l.setEscritor((input("Informe o nome do escritor: ")))
        l.setEstoque((input("Quantidade de estoque que deseja cadastrar: ")))
        livros.append(l)
        print("Livro cadastrado com sucesso no sistema")

    def mostralivro(self):
        for l in livros:
            print("Nome:",l.getNome(),"\nEscritor: ",l.getEscritor(),"\nCódigo: ",l.getCod(),"\nEm Estoque: ",l.getEstoque())
                  
     
###############################################################
class Empresta(Livro):
    def __ini__(self):
        Livro.__init__(self)
        self.qtd=int

    def getQuantidade(self):
        return self.qtd
    def setQuantidade(self,qtd):
        self.qtd=qtd    

    def emprestar(self):
        while True:
            
            codigo=self.setCod(input('Qual o código do livro:'))
            qtde=int(input('Qual a quantidade de livros:?'))
            v=0
            for liv in livros:
                #print(liv.getCod(),' - ',self.getCod())
                if liv.getCod() == self.getCod():
                    if int(liv.getEstoque()) > 0:
                        if qtde > int(liv.getEstoque()):
                            print("Quantidade de livro que esta pediindo não tem em estoque")
                            continue
                        else:

                            escolha=input('Deseja emprestar o livro?S/N:')
                            escolha==escolha.upper()

                            if escolha == 'S':
                                dep=int(liv.getEstoque()) - qtde
                                liv.setEstoque(dep)
                                print("livro empresatado")
                                continue
                    else:

                        print("Esse livro esta em falta")
                
                else:
                    print("Livro não encontrado")
            
            fecha = input('Deseja emprestar outro livro [S]IM OU [N]ÃO ?');

            if fecha == 'S':
                continue
            else:
                break    
                               
            
    def devolver(self):
        while True:

            cod  = (input('Qual o código do livro:'))
            qtde = int(input('Qual a quantidade de livros:?'))
            
            for liv in livros:
                if liv.getCod() == cod:
                     dep=int(liv.getEstoque()) + qtde
                     liv.setEstoque(dep)        
                     print("Livro Devolvido!")                                                
                     continue
                else:
                    print("Livro não encontrado")
                    continue
            
            fecha = input('Deseja devolver outro livro [S]IM OU [N]ÃO ?')

            if fecha == 'S':
                continue
            else:
                break         
                    
       
        

#########Programa Principal############################
def validamenu():
    print('-=-'*10)
    print('Sistema de Livros')
    print('-=-'*10)
    print(""" Menu de Navegação:
    0-  Sair
    1-  Cadastrar livro
    2-  Cadastrar Cliente
    3-  Listar Clientes
    4-  Listar Livros
    5-  Emprestar Livro
    6-  Devolver Livro
    
     
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

l=Livro()
c=Cliente()
e=Empresta()
# programa principal
while True:
    escolha = validamenu()
    if escolha ==0:
        print('Encerrando programa...')
        break
    elif escolha==1:
        l.cadastro()
    elif escolha==2:
        c.cadastroCli()
    elif escolha==3:
        c.listarC()
    elif escolha==4:
        l.mostralivro()
    elif escolha==5:
        e.emprestar()
    elif escolha==6:
        e.devolver()
            
   


 
               


