import joblib
from item import Item
from nltk import word_tokenize

#importando modelo pt-br
folder = 'trained_POS_taggers/'
teste_tagger = joblib.load(folder+'POS_tagger_brill.pkl')

phrase_file = open("frase.txt", "r")

frase = phrase_file.readline()

#array de objetos item
tokens = list()

#adiciona token a lista de tokens
for token in teste_tagger.tag(word_tokenize(frase)):
  tokens.append(Item(token[0], token[1]))
