from queue import PriorityQueue

class No:
    def __init__(self, char, frequencia):
        self.char = char
        self.frequencia = frequencia
        self.esq = None
        self.dir = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def tabela_frequencia(texto):
    tabela = {}
    for char in texto:
        tabela[char] = tabela.get(char, 0) + 1
    return tabela

def montar_arvore(tabela):
    fila_prioridade = PriorityQueue()
    for char, frequencia in tabela.items():
        fila_prioridade.put(No(char, frequencia))

    while fila_prioridade.qsize() > 1:
        primeiro = fila_prioridade.get()
        segundo = fila_prioridade.get()
        novo = No('+', primeiro.frequencia + segundo.frequencia)
        novo.esq = primeiro
        novo.dir = segundo
        fila_prioridade.put(novo)

    return fila_prioridade.get()

def gerar_codigo(raiz, codigo_atual, dic):
    if raiz is None:
        return

    if raiz.char != '+':
        dic[raiz.char] = codigo_atual
        return

    gerar_codigo(raiz.esq, codigo_atual + '0', dic)
    gerar_codigo(raiz.dir, codigo_atual + '1', dic)

def codificar(texto, dic):
    codigo = ''
    for char in texto:
        codigo += dic[char]
    return codigo

def decodificar(codigo, raiz):
    texto = ''
    atual = raiz
    for bit in codigo:
        if bit == '0':
            atual = atual.esq
        else:
            atual = atual.dir

        if atual.char != '+':
            texto += atual.char
            atual = raiz

    return texto

def main():
    texto = "O principio mais forte do crescimento reside na escolha humana."
    
    tabela = tabela_frequencia(texto)
    arvore = montar_arvore(tabela)
    dic = {}
    gerar_codigo(arvore, '', dic)
    codigo = codificar(texto, dic)
    texto_decodificado = decodificar(codigo, arvore)

    print("Texto original:", texto)
    print("Texto codificado:", codigo)
    print("Texto decodificado:", texto_decodificado)

if __name__ == "__main__":
    main()

