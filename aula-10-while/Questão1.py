#Escreva um programa que exiba os valores dos números de 1 até 100. Ao término o
#programa deverá exibir uma mensagem de encerramento informando que o programa
#terminou.

num = 0

botao = input('Digite s para iniciar: ')

if(botao == 's'):
    while (num < 100):
        num = num + 1
        print(num)
print('Fim do programa.')

