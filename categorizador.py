import joblib
from item import Item
from nltk import word_tokenize
class Categorizador:
  def __init__(self):
    #importando modelo pt-br
    folder = 'trained_POS_taggers/'
    self.teste_tagger = joblib.load(folder+'POS_tagger_brill.pkl')
    self.pontuacoes = [".", ",", ":", ";", "!", "?", "..."]
    self.preposicoes = ["da", "do", "na", "no", "pelo", "pela"]

  #gera tokens sem correção manual
  def tokenizar(self, frase):
    return self.teste_tagger.tag(word_tokenize(frase)) 

  #retorna tokens com correções para pontuações e preposições
  def get_tokens(self, frase):
    lista_tokens = list()

    #a análise do modelo pode falhar em preposições, etc... necessitando de correção manual
    for token, tipo in self.tokenizar(frase):
      #Preposição
      if token in self.preposicoes:
        tipo = "PREP"
      
      #Pontuação
      elif token in self.pontuacoes:
        tipo = "PUNCT"
      
      #adiciona token a lista de tokens formatada 
      subtoken = (token, tipo)
      lista_tokens.append(subtoken)
    
    #retorna token
    return lista_tokens

