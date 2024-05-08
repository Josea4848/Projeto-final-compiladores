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
      
      #recebendo lista de tokens
      tokens = Categorizador().get_tokens(frase)

      
      #tratando tokens e adicionando na árvore
      for token, tipo in tokens:
         if token == tipo:
            continue
         else: 
            if tipo == "N|EST":
               tipo = "N"
            elif tipo == "N|TEL":
               tipo = "NUM"
            elif tipo == "V|+":
               tipo = "V"

         #contatena tokens como gramática produção -> 'terminal'
         gramatica_particular += f"\n{tipo} -> '{token}'\n"


      gramatica_final = gramatica_geral + gramatica_particular 
      print(f"{gramatica_final}")
    
      # Criando um analisador sintático a partir da gramática
      self.gramatica = CFG.fromstring(gramatica_final)
      self.analisador = nltk.ChartParser(self.gramatica)

    # Função para realizar análise sintática de uma frase
    def analise_sintatica(self, frase):
        tokens = nltk.word_tokenize(frase)
        arvores = self.analisador.parse(tokens)
        contador = 0
        
        #iteração para as árvores
        for arv in arvores:
            if not arv:
                continue
            contador += 1
            arv.pretty_print()
            arv.draw()
  
        return contador
    
#definindo frase de entrada
frase = "a nova geração de iPad foi apresentada pela Apple"

#instanciando classe do analisador com a gramática
analisador = Sintatico("gramatica.mrg", frase)

#se returnar 0, a frase não está de acordo com a gramática
if not analisador.analise_sintatica(frase):
   print("A frase não está de acordo com a gramática especificada!")

