import random as aleatorio
from os import system, name 

#FUNÇÃO QUE FAZ A LIMPEZA DA TELA A CADA EXECUÇÃO
def limpa_tela():
    #Windows
    if name == 'nt':
        _= system('cls')
    #Mac ou Liux    
    else:
        _= system('clear')

#ESCOLHER A PALAVRA CONFORME A CLASSIFICAÇÃO SOLICITADA PELO USUÁRIO
def escolher_palavra(classificacao):
    palavras = {'frutas' : ['abacaxi', 'banana', 'laranja', 'morango', 'uva'], 
                'filmes' : ['velozesefuriosos', 'madmax', 'interestelar', 'questaodetempo', 'deadpool'],
                'paises' : ['brasil', 'africadosul', 'suiça', 'italia', 'argentina']}
    
    while True:
        if classificacao == 'frutas':
            return aleatorio.choice(palavras['frutas'])
        elif classificacao == 'filmes':
            return aleatorio.choice(palavras['filmes'])
        elif classificacao == 'paises':
            return aleatorio.choice(palavras['paises'])
        else:
            print("Escolha somente uma das opções anteriores!\n")
            break            

#INICIA O ADVINHE A PALAVRA
def jogar_advinhe_palavra():
    
    limpa_tela()

    print("\n-------------------| SEJA BEM VINDO AO ADVINHE A PALAVRA |-------------------")
    jogar = input("Deseja jogar? (S|N) ").lower()
    
    if jogar == 's' or jogar == 'sim':
        
        while True:
            limpa_tela()
            
            print("\nEscolha uma das classificações abaixo: \n"
                "Opção 1: Frutas\n"
                "Opção 2: Filmes\n"
                "Opção 3: Paises\n")
            
            classificacao = input("Escolha a opçao: ").lower()
            palavra_secreta = escolher_palavra(classificacao)
            
            while True:        
                if palavra_secreta == None:
                    classificacao = input("\nDigite novamente a opção: ").lower()
                    palavra_secreta = escolher_palavra(classificacao)                   
                else: 
                    letras_descobertas = ['-' for letras in palavra_secreta]
                    letras_digitadas = []
                    letras_erradas = []
                    tentativas = 10
                    break

            print("\nOpção escolhida: ", classificacao.upper())

            while tentativas > 0:
                
                print("PALAVRA: "," ".join(letras_descobertas))
                print("TENTATIVAS: ", tentativas)
                print("LETRAS INCORRETAS:", " ".join(letras_erradas))

                letra = input("\nDigite uma letra: ").lower()

                if letra in letras_digitadas:
                    print("Você já digitou essa letra!\n")
                    continue
                elif letra in palavra_secreta:
                    print("Acertou!\n")
                    index = 0
                    for let in palavra_secreta:
                        if letra == let:
                            letras_descobertas[index] = letra
                        index += 1
                else:
                    print("Errou!\n")
                    tentativas -= 1
                    letras_erradas.append(letra)
                
                letras_digitadas.append(letra)

                if set(palavra_secreta).issubset(set(letras_digitadas)):
                    print("\nParabéns! Você acertou a palavra secreta:", palavra_secreta.upper())
                    break
                
                elif tentativas == 0:
                    print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
                    break
            
            jogar_novamente = input("\nDeseja jogar novamente ? (S|N) ").lower()

            if jogar_novamente == 's' or jogar_novamente == 'sim':
                continue
            elif jogar_novamente == 'n' or jogar_novamente == 'nao':
                print("Obrigado por jogar! Até a próxima...")
                limpa_tela()
                break
            else:
                print("Digite somente (S|N)")
                limpa_tela()
        
    elif jogar == 'n' or jogar == 'nao':
        print("\nSaindo...")
        limpa_tela()
    else:
        print("\nDigite somente (S|N)")
        limpa_tela() 

#DIZ QUE O MÓDULO EXECUTÁVEL É O "jogar_advinhe_palavra"
if __name__ == "__main__":
    jogar_advinhe_palavra()