import adivinhacao
import forca

def escolha_jogo():
    print("*****************************")
    print("     Escolha o seu jogo!     ")
    print("*****************************")

    print("[1] Forca")
    print("[2] Adivinhacao")

    jogo = int(input("Qual o jogo desejado?"))

    if jogo == 1:
        print("Jogo escolhido: Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogo escolhido: Adivinhacao")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolha_jogo()