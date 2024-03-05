'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''

notas = int(input("Digite sua nota: "))
presenca= int(input("Digite sua presenca: "))

if notas < 6:
    print(notas,"reprovado")
else:
    print(notas ,"aprovado")
