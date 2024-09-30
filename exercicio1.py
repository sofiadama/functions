def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(inicio)
            inicio += passo
    else:
        while inicio >= fim:
            print(inicio)
            inicio -= passo

print('Contagem de 1 a 10 de 1 em 1: \n')

contador(1,10,1)
print()

print('Contagem de 10 a 0 de 2 em 2: \n')

contador(10,0,2)
print()

print('Contagem personalizada: \n')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print()
contador(inicio,fim,passo)


