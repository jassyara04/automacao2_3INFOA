'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

contador = 1
grupos1 = []
grupos2 = []
grupos3 = []

while True:
    matricula = int(input('Digite a matricula: '))


    if matricula == 0:
        break 

    if contador == 1:
        grupo1.append(matricula)
    elif contador == 2:
        grupo2.append(matricula)
    elif contador == 3:
        grupo3.append(matricula)
        contador = 0

    contador = contador + 1


print("Grupo 1", grupos[0])
print("Grupo 2", grupos[1])
print("Grupo 3", grupos[2])