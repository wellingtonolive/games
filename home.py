import forca
import adivinhacao


def change_game():
    print("*********************************")
    print("Escolha o seu jogo !!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.play()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.play()


if __name__ == "__main__":
    change_game()
