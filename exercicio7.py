def capacidade(N,C):
    pessoas = N
    for _ in range(N):
        S = int(input("Saídas: "))
        E = int(input("Entradas: "))
        
        pessoas -= S
        pessoas += E
        
        if pessoas > C:
            print("S")
        else:
            print("N")
            
N = int(input("Leituras: "))
C = int(input("Capacidade máxima: "))
                  
capacidade(N,C)