""""
Construir um algoritmo que contenha 3 listas:
• Nomes de produtos
• Preços de cada produto
• Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas
"""

### Listas###
nomeproduto=['mandolate']
preco=[]
quantidade=[]
menu=[0,1,2,3]

def validamenu():
    print ( """         
    --------------------------
            Menu 
    ~~~~~~~~~~~~~~~~~~~~~~~~~
            0- Encerrar         
            1- Cadastrar
            2- Retirar
            3- Imprimir
    --------------------------        
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


def cadastrar():
    produto=input("Digite o nome do produto: ")
    nomeproduto.append(produto)
    print("Produto disponíveis: ",produto)

def imprimir():
    print("Produtos Cadastrados")
    print(nomeproduto)


def retirar():
    print(nomeproduto)
    produto_del=input("Digite o produto a ser deletado: ")
    if produto_del in nomeproduto:
        index=nomeproduto.index(produto_del)
        nomeproduto.pop(index)
        print("Produto deletado com sucesso")

    else:
        print("Produto não encontrado")

   
        

#####MENU PRINCIPAL######
while True:
    escolha = validamenu()
    if escolha ==0:
        print('Encerrando programa...')
        break
    elif escolha==1:
        cadastrar()
    elif escolha==2:
        retirar()
    elif escolha==3:
        imprimir()
   

    
