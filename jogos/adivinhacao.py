import random

def escolher_nivel():
    while True:
        print("Qual a dificuldade desejada?")
        print("[1] Facil (20 Tentativas)")
        print("[2] Medio (10 Tentativas)")
        print("[3] Dificil (5 Tentativas)")

        try:
            nivel = int(input("Defina o nivel: "))
            if nivel == 1:
                tentativas = 20
                return tentativas
            elif nivel == 2:
                tentativas = 10
                return tentativas
            elif nivel == 3:
                tentativas = 5
                return tentativas
            else:
                print("Erro: Defina um nivel valido")
        
        except ValueError:
            print("Erro: digite um número válido.")

def jogar():
    print("************************************")
    print("  Bem vindo ao jogo de Adivinhacao  ")
    print("************************************")
    print("Acerte o numero aleatorio de 1 a 100")
    print("************************************")

    numero_secreto = random.randint(1, 100)
    tentativas = escolher_nivel()
    rodada = 1
    pontos = 1000

    print("\nVoce tem {} tentativas!!!".format(tentativas))

    for rodada in range (1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        try:
            chute = int(input("Digite o seu numero: "))
            print("Voce digitou:", chute)

            acerto = numero_secreto == chute
            maior  = numero_secreto < chute
            menor  = numero_secreto > chute

            if acerto:
                print("Voce acertou!!!\n")
                print("Voce fez {} pontos!!!".format(pontos))
                break
            elif chute < 1 or chute > 100:
                print("Erro: Voce deve digitar um numero entre 1 e 100\n")
                continue
            else:
                if maior:
                    print("Seu chute foi maior que o numero secreto!\n")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos
                elif menor:
                    print("Seu chute foi menor que o numero secreto!\n")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos

        except ValueError:
            print("Erro: digite um número válido.")

        rodada = rodada + 1

    print("Fim de Jogo\n")

    jogar_novamente = input("Deseja jogar novamente?[s/n]")
    while jogar_novamente.lower() not in ["s", "n"]:
        print("Opcao invalida, digite 's' para sim ou 'n' para nao.")
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente == "s":
        jogar()
    else:
        print("Obrigado por jogar!")

if(__name__ == "__main__"):
    jogar()