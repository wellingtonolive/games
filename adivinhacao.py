print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 45
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas+1):

    print('Tentativa {} de {}:'.format(rodada, total_de_tentativas))

    palpite_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou o seguinte valor ", palpite_str)

    chute = int(palpite_str)

    if chute < 1 or chute > 100:
        print("Valor Inválido. Você deve digitar um valor entre 1 e 100 !!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você Acertou !!!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o numero secreto.")
        print("Você Errou !!!")

print("*********************************")
print("******** Fim do Jogo ************")
print("*********************************")
