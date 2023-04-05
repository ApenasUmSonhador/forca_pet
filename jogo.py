from os import name, system

forca = True
palavra_formada = ''

def limpar():
    if name == "nt":
        system('cls')
    else:
        system('clear')
        
while forca == True:
    vitoria = False
    tentativas = 0
    letras_acertadas = []
    letras_tentadas = []
    palavra_secreta = input("Bem vindo ao jogo da forca, escolha (escondido), a palavra para seus amigos acertarem!\n").strip().lower()
    while len(palavra_secreta) <1 or not palavra_secreta.isalpha():
        input("Digite uma palavra válida (formada apenas por letras): \n")
    limpar()
    
    while vitoria == False:
        if tentativas >0:
            print("Letras já tentadas: ",letras_tentadas)

        letra_chutada = input("Digite uma letra: \n").strip().lower()
        tentativas+=1
        ultima_formada = palavra_formada
        palavra_formada = ''

        if len(letra_chutada)>1 or not letra_chutada.isalpha():
            print("\nChute UMA LETRA apenas.")
            print("Palavra ainda é: ", ultima_formada)
            tentativas -=1
            continue

        elif letra_chutada in letras_tentadas:
            print("\nVocê já chutou essa letra antes, tente outra.")
            print("Palavra ainda é: ", ultima_formada)
            tentativas -=1

        else:
            letras_tentadas.append(letra_chutada)
            if letra_chutada in palavra_secreta:
                letras_acertadas.append(letra_chutada)
                for letra_secreta in palavra_secreta:
                    
                    if letra_secreta in letras_acertadas:
                        palavra_formada += letra_secreta
                        
                    else:
                        palavra_formada += ' *'
                
            else:
                print("\nVoce errou, tente de novo")
                print("Palavra ainda é: ", ultima_formada)

            print("Palavra formada: ", palavra_formada)
            print("Tentativas: ", tentativas)
            
            if palavra_formada  == palavra_secreta:
                limpar()
                vitoria = True
                
                print("Parabéns voce ganhou!!")
                print("A palavra era: ", palavra_secreta)
                print("Voce conseguiu em: ",tentativas)
                
                forca = input("Deseja jogar novamente? [s]im [n]ao.\n").strip().lower().startswith('s')
