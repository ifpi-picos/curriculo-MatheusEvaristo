def listarAtletas(listaDeAtletas):
   for i, Atletas in enumerate(atletas, 1):
       print(i,Atletas)

atletas = []
print('lista de atletas:')
atletas.append('0 - Paulo')
atletas.append('1 - Marcos')
atletas.append('2 - João')
atletas.append('3 - Carlos')

print(atletas)

print('escolha um alteta:')
AtletaEscolhido = int(input())

def listarPatrocinador(listaDePatrocinadores):
   for i, patrocinador in enumerate(patrocinador):
       print(i,patrocinador)

patocinadores = []
print('lista de patocinadores:')
patocinadores.append('4 - Nike')
patocinadores.append('5 - Adidas')

print(patocinadores)

print('escolha um patrocinador:')
PatrocinadroEscolhido = int(input())

def divisao(n1, n2):
   resultado = n1 / n2
   return resultado

def ValorDoPatrocinio():
   return float(input('Valor:'))

def ValorParcelas():
   return float(input('Parcela:'))

while True:
   n1 = ValorDoPatrocinio()
   n2 = ValorParcelas()
   print(divisao(n1, n2))
   break