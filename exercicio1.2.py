def dim_colchao_e_porta(A,B,C,H,L):
    colchao = A*B*C
    porta = H*L
    if porta >= colchao:
        print("S")
    else:
        print("N")
    return colchao,porta

A,B,C = map(int,input().split())
H,L = map(int,input().split())

dim_colchao_e_porta(A,B,C,H,L)



