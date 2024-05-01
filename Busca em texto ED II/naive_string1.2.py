def naive_string(frase,chave):
    n = len(frase)
    m = len(chave)
    oc = []
    for i in range(n - m + 1):
        igual = True
        for j in  range(m):
            if chave[j] != '*' and frase[i + j] != chave[j]:
                igual = False
                break
        if igual:
            oc.append(i)
    return oc
    
frase = "O rato roeu a roupa do rei de roma"
chave = "ro**"
ocorrencias = naive_string(frase,chave)
print(f"Ocorrências do padrão {chave} na frase {frase} : {ocorrencias}")
