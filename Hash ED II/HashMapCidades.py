cidade = []
primo = 67
i = 0
colisao = 0
for i in range(primo):
    cidade.append(0)

def indicehash(chave, primo):
    key = codASCII(chave)
    return key % primo

def codASCII(chave):
    soma = 0
    for caractere in chave:
        soma += ord(caractere)
    return soma

def numeroColisao(nomes, numeroColisao):
  acc = 0
  if numeroColisao == 10:
     for name in nomes:
        if name >= numeroColisao:
           acc +=1
     return acc
  for name in nomes:
    if name == numeroColisao:
      acc += 1
  return acc

nomes = []
with open("cidades.txt", "r") as arquivo:
  linhas = arquivo.readlines()
  for linha in linhas:
    nomes.append(linha.strip())

for nome in nomes:
   resultado = indicehash(nome, primo)
   cidade[resultado] += 1
   if(cidade[resultado] > 1):
      colisao+= 1
      
print(cidade)
print("Indices com 0 cidades:", numeroColisao(cidade, 0))
print("Indices com 1 cidades:", numeroColisao(cidade, 1))
print("Indices com 2 cidades:", numeroColisao(cidade, 2))
print("Indices com 3 cidades:", numeroColisao(cidade, 3))
print("Indices com 4 cidades:", numeroColisao(cidade, 4))
print("Indices com 5 cidades:", numeroColisao(cidade, 5))
print("Indices com 6 cidades:", numeroColisao(cidade, 6))
print("Indices com 7 cidades:", numeroColisao(cidade,7))
print("Indices com 8 cidades:", numeroColisao(cidade, 8))
print("Indices com 9 cidades:", numeroColisao(cidade, 9))
print("Indices com mais de 10 cidades:", numeroColisao(cidade, 10))
acc = 0
for nome in cidade:
   if nome > 1:
      acc += nome
print("Total de colisões: ",colisao)