class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None

class TabelaHash:
    def __init__(self, tam_tabela, tam_max):
        self.tabela = [None for _ in range(tam_tabela)]
        self.tam_max = tam_max
        self.colisoes = 0
        self.enderecos_com_cidades = [0] * 11

    def funcao_hash(self, chave):
        parte_chave = 4
        soma = 0
        chave_inversa = chave[::-1]
        for i in range(0,len(chave_inversa),parte_chave):
            parte = chave_inversa[i:i+parte_chave]
            soma_parte = 0
            for caractere in parte:
                soma_parte += ord(caractere)
            soma += soma_parte
            
        return soma % len(self.tabela)

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = No(chave)
        else: 
            self.colisoes += 1
            atual = self.tabela[indice]
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = No(chave)

    def calcular_estatisticas(self):
        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                numero_cidades = 0
                aux = self.tabela[i]
                while aux is not None:
                    numero_cidades += 1
                    aux = aux.prox
                self.enderecos_com_cidades[numero_cidades] += 1

    def imprimir_estatisticas(self):
        print(f"Número de colisões: {self.colisoes}")
        for i in range(1, len(self.enderecos_com_cidades)):
            print(f"Endereços com {i} cidades: {self.enderecos_com_cidades[i]}")
            
    def imprimir_tabela(self):
        for i,elemento in enumerate(self.tabela):
            if elemento is not None and elemento.prox is not None:
                print(f"Posição {i} ", end= "")
                while elemento is not None:
                    print(elemento.chave, end= " -> ")
                    elemento = elemento.prox
                print("None")

primo = 839
nomes = []
with open("Hash ED II/cidades.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        nomes.append(linha.strip())

table = TabelaHash(primo, 11)

for nome in nomes:
    table.inserir(nome)

table.calcular_estatisticas()
table.imprimir_estatisticas()

print("\nTabela Hash: \n")
table.imprimir_tabela()
