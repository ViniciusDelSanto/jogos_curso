def jogar():
    print("*****************************")
    print(" Bem Vindo ao Jogo da Forca! ")
    print("*****************************")

    palavra = "banana"
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False
    acertou = False

    print(letras_certas)
    
    # while True e True
    while not enforcou and not acertou:

        chute = input("Digite uma letra:")
        chute = chute.strip()

        index = 0
        for letra in palavra:
            if chute.upper()== letra.upper():
                letras_certas[index] = letra
            index = index + 1
        print(letras_certas)


    print("Fim de Jogo")


if(__name__ == "__main__"):
    jogar()