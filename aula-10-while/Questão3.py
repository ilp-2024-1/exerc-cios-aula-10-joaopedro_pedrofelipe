#Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor
#com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor
#da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a
#senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar
#que o usuário acertou a senha.

csenha = input('Crie uma senha: ')
print('Senha criada')

senha = input('Digite a senha: ')

while(senha != csenha):
    senha = input('Digite a senha: ')

print('Você acertou a senha. Fim do programa.')