""" ### Exericício 1
Construa um algoritmo que possua uma tupla com os números escritos por extenso de “zero” a “nove”.
Peça ao usuário para digitar um nome de 0 a 9 e retorne a ele o número por extenso,
sem usar estruturas condicionais (if e switch).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove')
numero = int(input('Digite um numero de 0 a 9: '))
while numero not in range(0,10):
	numero = int(input('Tente novamente.\nDigite um numero de 0 a 9: '))

print(f'Você digitou o número {extensos[numero]}!')

"""

#########################################################################

""" ####Exércicio 2

▷Construa um algoritmo que peça ao usuário para informar o nome, a nota01 e a nota02 de um aluno.
Guarde estas informações em um dicionário.
Após, calcule a nota final deste aluno [(nota01 + nota02) /2] e adicione ao dicionário.
Ao final, imprima todos os dados do dicionário.

"""
dados=dict()
dados= {}
dados['nome']=str(input("Digite o nome do aluno: " ))
dados['nota01']=int(input("Digite a nota 01 do aluno: "))
dados['nota02']=int(input("Digite a nota 02 do aluno: "))
dados['notafinal']=nota01 + nota02/2
print("Dados cadastrados no dicionário: ",dados)


