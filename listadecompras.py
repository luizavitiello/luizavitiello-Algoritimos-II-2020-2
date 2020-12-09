"""Construir um algoritmo que permite que o usuário informe uma lista de produtos para serem comprados em um supermercado
( lista de compras).
Os nomes dos produtos devem ser salvos em um arquivo de texto
e a lista poderá ser modificada sempre que o usuário quiser.
"""

listac=['feijao']
arquivo=open("lista.txt","w")
while True:
    i=input("Insira os itens para compra: ")
    listac.append(i)
    print("Lista Atual:",listac)
    print("item add a lista com sucesso")
    for i in range (len(listac)):
        exporta=(str(listac))
        arquivo.write(exporta)
    p=input("deseja continuar? s/n: ")
    if p =='s':
        pass
    elif p=='n':
        break
   
arquivo.close()
