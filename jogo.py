from os import name, system

forca = True

def limpar():
    if name == "nt":
        system('cls')
    else:
        system('clear')
        
while forca == True:
    vitoria = False
    tentativas = 0
    letras_acertadas = ''
    
    palavra_secreta = input("Bem vindo ao jogo da forca, escolha (escondido), a palavra para seus amigos acertarem!")
    limpar()
    
    while vitoria == False:
        letra_chutada = input("Digite uma letra: ")
        tentativas+=1
        palavra_formada = ''
        
        if len(letra_chutada)>1 or len(letra_chutada) == 0 or not letra_chutada.isalpha():
            print("Chute UMA LETRA apenas.")
            continue
        else:
            if letra_chutada in palavra_secreta:
                letras_acertadas+=letra_chutada
                for letra_secreta in palavra_secreta:
                    
                    if letra_secreta in letras_acertadas:
                        palavra_formada += letra_secreta
                        
                    else:
                        palavra_formada += '*'
                        
                print("Palavra formada: ", palavra_formada)
                
            else:
                print("Voce errou, tente de novo")
            print("Tentativas: ", tentativas)
            
            if palavra_formada  == palavra_secreta:
                limpar()
                vitoria = True
                
                print("Parabéns voce ganhou!!")
                print("A palavra era: ", palavra_secreta)
                print("Voce conseguiu em: ",tentativas)
                
                forca = input("Deseja jogar novamente? [s]im [n]ao").strip().lower().startswith('s')
