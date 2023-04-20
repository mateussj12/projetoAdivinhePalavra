# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos
# Classe Forca

# Import
from os import system, name 
import random as aleatorio

# Método limpar tela
def limpa_tela():
     if name == 'nt':
          _= system('cls')
     else:
          _= system('clear') 

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:

	# Método Construtor
     def __init__(self):
          self.letras_certas = []
          self.letras_erradas = []

     # Classificação de palavras
     def escolher_palavra(self, classificacao):
     
          palavras = {
          
          'frutas' : ['abacaxi', 'banana', 'laranja', 'morango', 'uva'], 
          'filmes' : ['superman', 'madmax', 'interestelar', 'batman', 'deadpool'],
          'paises' : ['brasil', 'eua', 'suiça', 'italia', 'argentina']
          
          }
          
          while True:
               if classificacao == 'frutas':
                    return aleatorio.choice(palavras['frutas'])
               elif classificacao == 'filmes':
                    return aleatorio.choice(palavras['filmes'])
               elif classificacao == 'paises':
                    return aleatorio.choice(palavras['paises'])
               else:
                    print("Digite apenas uma das opções anteriores\n")
                    break             

	# Método para adivinhar a letra
     def adivinha_palavra(self, letra, palavra):
          if letra in palavra:
               self.letras_certas.append(letra)
          else:
               self.letras_erradas.append(letra)     
		
	# Método para verificar se o jogador venceu
     def jogador_venceu(self, palavra):
          return set(self.letras_certas) == set(palavra)

     # Método para verificar se o jogador perdeu
     def jogador_perdeu(self):
          return len(self.letras_erradas) == 7

     # Método para mostrar as letras certas
     def let_certas(self, palavra):
          campo = ''
          for letra in palavra:
               if letra in self.letras_certas:
                    campo += letra
               else:
                    campo += "-"

          return campo         

     # Método para mostrar letras erradas
     def let_erradas(self, palavra):
          campo = ''
          for letra in self.letras_erradas:
               if letra != palavra:
                    campo += letra
               else:
                    campo += ''
          return campo               

     # Método para mostrar o tabuleiro
     def board(self):
          print(board[len(self.letras_erradas)])
