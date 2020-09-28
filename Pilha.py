from No import No

# inserir na pilha
# remover da pilha
# observar o topo da pilha

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0

    def inserir(self,elem):
        #insere um elemento na pilha
        no=No(elem)
        no.next=self.top
        self.top=no 
        self.size=self.size+1

    def remover(self):
        #remove o elemento no topo da pilha
        if self.size >0:
            no=self.top
            self.top=self.top.next
            self.size=self.size-1
            print("Pilha removida com suucesso")
            return no
        else:
           print ("A pilha está vazia!")

    def imprimir(self):
        print self.dado