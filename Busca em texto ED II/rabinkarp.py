def rabin_karp(T,P,d,q):
    n = len(T)
    m = len(P)
    h = d ** (m - 1)
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(n - m + 1):
        if p == t:
            igual = True
            for i in range(m):
                if P[i] != T[s + i]:
                    igual = False
                    break
            if igual:
                print(f"Padrão encontrado na posição {s}")
        if s < n - m:
            t = (d * (t - ord(T[s])* h) + ord(T[s + m])) % q
            
frase = "ababcababcabc"
chave = "abc"
d = 256
q = 2
rabin_karp(frase,chave,d,q)
            
    