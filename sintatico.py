from item import Item
from time import sleep

class Sintatico:
  def __init__(self, tokens):
    self.tokens = tokens
    self.posicao = 0 #posição do token
    self.token = tokens[self.posicao]
    self.erros =  list()
    self.dados = ['ADJ', 'ADV', 'ADV-KS', 'ADV-KS-REL', 'ART', 'KC', 'KS', 'IN', 'N', 'NPROP', 'NUM', 'PCP', 'PDEN', 'PREP', 'PROADJ', 'PRO-KS', 'PROPESS', 'PRO-KS-REL', 'PROSUB', 'V', 'VAUX', 'CUR', 'EST', 'AP', 'DAD', 'TEL', 'DAT', 'HOR', '[' ,']', '+']
    self.pontuacao = ['!', '.', '...']

  #avança token
  def next_token(self):
    if self.posicao + 1 < len(self.tokens):
      self.posicao += 1
      self.token = tokens[self.posicao]

  def texto(self):
    self.sentenca()
    #verifica último terminal, tem que terminar com pontuação
    if self.token.getType() not in self.pontuacao:
      self.erros.append("faltando pontuação")
    else:
      self.next_token()
      #verifica se contém outro texto
      if self.token.getType() in self.dados:
        print(f"P: {self.token.getWord()}, T: {self.token.getType()}")
        #sleep(5000)
        self.texto()
    
    

  def sentenca(self):
    #setenca -> sintagma_nominal sintagma_verbal
    self.sintagma_nominal()
    print(f"INDO PRA VERBAL {self.token.getWord()}, {self.token.getType()}")
    self.sintagma_verbal()
    print("FIM KKKKK")

  def sintagma_nominal(self):
    #sintagma_nominal -> adjunto_adnominal nome adjunto_adnominal 
    #nome -> N | NPROP | PROSUB | PROPESS
    
    
    self.adjunto_adnominal()
    print(f'sn -> token: "{self.token.getWord()}, {self.token.getType()}')

    if self.token.getType() != 'N' and self.token.getType() != 'NPROP' and self.token.getType() != 'PROPESS' and self.token.getType() != 'PROSUB':
      print(f"Palavra: {self.token.getWord()}, tipo: {self.token.getType()}")
      self.erros.append(f"{self.token.getType()} faltando nome")
    else:
      self.next_token()
      self.adjunto_adnominal()
      
      #sleep(5000)

  def adjunto_adnominal(self):
    #adjunto_adnominal -> adjuntos adjunto_adnominal
    #adjuntos -> ADJ | ADV | ADV-KS | ADV-KS-REL | ART | NUM | PDEN | PROADJ | PRO-KS | PRO-KS-REL 

    print(f'aa -> token: "{self.token.getWord()}, {self.token.getType()}')
    adjuntos = ['ADJ', 'ADV', 'ADV-KS', 'ADV-KS-REL', 'ART', 'NUM', 'PDEN', 'PROADJ', 'PRO-KS', 'PRO-KS-REL']
    
    if self.token.getType() in adjuntos:
      self.next_token()
      print(f"KKKKKKKK {self.token.getWord()}, {self.token.getType()}")

  def sintagma_verbal(self):
    #sintagma_verbal -V NP PP | V ADV
    
    if(self.token.getType() != 'V'):
      self.erros.append("faltando verbo")
    else:    
      self.next_token()
    
    #breakpoint()
    if(self.token.getType() not in ['ADV','ADJ']):
      print("cheguei")
      print(f'c -> token: "{self.token.getWord()}, {self.token.getType()}')
      #sleep(5000)
      self.sintagma_preposicional()
    #Teve um advérbio (ADV) ou Adjetivo
    elif self.token.getType() != 'ADJ':
      print(f"HAHAHAHA {self.token.getWord()}")
      self.next_token()
      if self.token.getType() == "ART":
        self.sintagma_nominal()
    else:
      print(f"FIM Palavra: {self.token.getWord()}, Type: {self.token.getType()}")
      self.next_token()
      print(f"FIM Palavra: {self.token.getWord()}, Type: {self.token.getType()}")
    
    if self.token.getType() == "KC":
      self.next_token()
      self.sintagma_verbal()

  def sintagma_preposicional(self):
    print(f'sp -> token: "{self.token.getWord()}, {self.token.getType()}')
    #sleep(5000)
    #sintagma_preposicional -> P NP
    if self.token.getType() == "PREP":
      self.next_token()
      self.sintagma_nominal()
  

tokens_file = open("tokens.txt", "r")
tokens = list()

for line in tokens_file:
  line = line.replace("\n", "")
  sublist = line.split("\pu")
  tokens.append(Item(sublist[0], sublist[1]))

sintatico = Sintatico(tokens)
sintatico.texto()

if len(sintatico.erros):
  print(sintatico.erros)