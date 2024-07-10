#Escreva um programa que solicita ao usuário valores numéricos e realiza a soma
#desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do
#somatório e encerrar o programa com uma mensagem de término do programa. O
#usuário deverá ser informado no início do programa o que o programa faz e qual a
#condição para encerramento do programa.

soma = 0
print('Faça a soma, quamdo quiser saber o resultado digite 0')
num = float(input('Digite o numero: '))

while(num != 0):
    soma = soma + num
    num = float(input('Digite o numero: '))

print('Esse é o resultado: ', soma)

print('Fim do programa')

