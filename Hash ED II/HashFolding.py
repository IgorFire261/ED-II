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
        # Implement folding hash method with segments in reverse order
        soma = 0
        for i in range(len(chave)-2, -1, -2):
            segment = chave[i:i+2]  # Partition key into segments of 2 characters
            reversed_segment = segment[::-1]  # Reverse the segment
            # Remove leading zeros
            reversed_segment = reversed_segment.lstrip('0')
            # Check if segment is empty after removing leading zeros
            if reversed_segment:
                soma += int(reversed_segment)  # Convert to integer and then sum;
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

primo = 239
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
