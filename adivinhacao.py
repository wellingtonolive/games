print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 4543

palpite = input("Digite o seu palpite: ")

print("Você digitou o seguinte valor ", palpite)

valor_inteiro = int(palpite)

if valor_inteiro == numero_secreto:
    print("Você Acertou !!!")
else:
    print("Você Errou !!!")


print("*********************************")
print("******** Fim do Jogo ************")
print("*********************************")