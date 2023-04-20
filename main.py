# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos
# Arquivo de execução
from classes import classe_forca

# Corpo jogo
def jogar():

    print("\n-------------------| ADVINHE A PALAVRA |-------------------")
    jogar = input("Deseja jogar? (S|N) ").lower()
    if jogar == 's' or jogar == 'sim':
        
        classe_forca.limpa_tela()

        # Executa o jogo enquanto o jogador decidir encerrar
        while True:
            
            # Cria o objeto 
            jogo = classe_forca.Hangman()    
            
            classe_forca.limpa_tela()

            # Mostra as opções na tela para o jogador e recebe a opção escolhida
            print("\nEscolha uma das classificações abaixo: \n"
                "Opção 1: Frutas\n"
                "Opção 2: Filmes\n"
                "Opção 3: Paises\n")
            
            classificacao = input("Escolha a opçao: ").lower()
            palavra = jogo.escolher_palavra(classificacao)

            # Executa a escolha de opções até o jogador digitar a opção correta
            while True:        
                if palavra == None:
                    classificacao = input("\nDigite novamente a opção: ").lower()
                    palavra = jogo.escolher_palavra(classificacao)                 
                else: 
                    break

            classe_forca.limpa_tela()

            # Executa as tentativas até o usuário acertar a palavra ou atingir a quantidade de tentativas, vença ou perca
            while not jogo.jogador_venceu(palavra) and not jogo.jogador_perdeu():

                classe_forca.limpa_tela()
                
                # Mostra na tela a opção escolhida        
                print("\nOpção escolhida: ", classificacao.upper())

                # Statyus do jogo
                jogo.board()
                print("\nPALAVRA: ", jogo.let_certas(palavra).upper())
                print("LETRAS ERRADAS: ", " ".join(jogo.let_erradas(palavra)).upper())

                # Recebe a letra
                letra = input("\nDigite uma letra: ").lower()
                jogo.adivinha_palavra(letra, palavra)
                
                # Procedimentos
                if jogo.jogador_venceu(palavra):
                    print("\nParabens! Você acertou a palavra", palavra.upper())
                    break
                elif jogo.jogador_perdeu():
                    print("\nVocê perdeu!, palvara correta era: ", palavra.upper())
                    break
                else:
                    classe_forca.limpa_tela()
                    continue  

            #Recebe e valida se o jogador vai querer jogar novamente    
            jogar_novamente = input("\nDeseja jogar novamente ? (S|N) ").lower()
            if jogar_novamente == 's' or jogar_novamente == 'sim':
                classe_forca.limpa_tela()
                pass
            elif jogar_novamente == 'n' or jogar_novamente == 'nao':
                print("Obrigado por jogar! Até a próxima...")
                classe_forca.limpa_tela()
                break
            else:
                print("Digite somente (S|N)")

    elif jogar == 'n' or jogar == 'nao':
        print("\nSaindo...")
        classe_forca.limpa_tela()

    else:
        print("\nDigite somente (S|N)")

# Executa o método "jogo" como principal
if __name__ == "__main__":
    jogar()       


