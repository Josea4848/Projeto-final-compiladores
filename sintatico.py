from nltk import CFG
from nltk import draw
import nltk
from nltk.parse import ChartParser
import joblib
from nltk import word_tokenize
from categorizador import Categorizador
from time import sleep

class Sintatico:
    def __init__(self, gramatica, frase):
      gramatica_file = open("gramatica.mrg", "r")
      gramatica_geral = gramatica_file.read()
      gramatica_particular = ""
      

      tokens = Categorizador().get_tokens(frase)

      for token, tipo in tokens:
        if token == tipo:
           continue
        else: 
           gramatica_particular += f"\n{tipo} -> '{token}'\n"

    
      gramatica_final = gramatica_geral + gramatica_particular 
      print(f"{gramatica_final}")
    
      # Criando um analisador sintático a partir da gramática
      self.gramatica = CFG.fromstring(gramatica_final)
      self.analisador = nltk.ChartParser(self.gramatica)

    # Função para realizar análise sintática de uma frase
    def analise_sintatica(self, frase):
        
        tokens = nltk.word_tokenize(frase)

        print(tokens)

        trees = self.analisador.parse(tokens)

        count = 0
        for tree in trees:
            if not tree:
                continue
            count += 1
            tree.pretty_print()
            tree.draw()
  

        return count

#nova gera ̧c ̃ao de iPad foi apresentada por Apple

frase = "a nova geração de iPad foi apresentada pela Apple"

analisador = Sintatico("gramatica.mrg", frase)

if analisador.analise_sintatica(frase):
   print("frase errada")

  #saí rapidão