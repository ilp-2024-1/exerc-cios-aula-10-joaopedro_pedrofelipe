#Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
#para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
#o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
#necessários e informar que o programa encerrou.

import random

num_ale = random.randint(0, 10)
print(num_ale)

num_test = int(input('Advinhe o numero: '))

while(num_ale != num_test):
    num_test = int(input('tente novamente: '))

print('Você acertou')

print('Fim do programa')
