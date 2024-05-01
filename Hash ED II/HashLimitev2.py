def inverter(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def ASC(nome_cidade):
    valorASC = 0
    for caractere in nome_cidade:
        valorASC += inverter(ord(caractere))
    return valorASC

def indice_hash(cidade, primo):
    chave = ASC(cidade)
    hash_valor = chave % primo
    return hash_valor

primo = 839
cidades = []
colisoes = 0
vetor = [[] for _ in range(primo)]


with open("Hash ED II/cidades.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        cidade = linha.strip()
        posicao = indice_hash(cidade, primo)
        vetor[posicao].append(cidade)
        
        if len(vetor[posicao]) > 1:
            colisoes += 1

ocupacao = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for i in range(len(vetor)):
    if len(vetor[i]) > 10:
        ocupacao[10] += 1
    else:
        ocupacao[len(vetor[i])] += 1    

for i in range(len(ocupacao)):
    print("Endereços com", i, "cidades:", ocupacao[i])
print("Houve {} colisões".format(colisoes))