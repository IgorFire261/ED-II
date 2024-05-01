def rabin_karp(T,P,d,q):
    n = len(T)
    m = max(len(P) for p in P)
    h = d ** (m - 1)
    for pattern in P:
        m = len(pattern)
        p = 0
        t = 0
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(T[i])) % q

        for s in range(n - m + 1):
            if p == t:
                match = True
                for i in range(m):
                    if pattern[i] != T[s + i]:
                        match = False
                        break
                if match:
                    print(f"Padrão '{pattern}' encontrado na posição {s}")

            if s < n - m:
                t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
            
frase = "O rato roeu a roupa do rei de roma abcaaabcbbbabc"
chave = ["rato","rei","abc"]
d = 256
q = 2
rabin_karp(frase,chave,d,q)
            
    