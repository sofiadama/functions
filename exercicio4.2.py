def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contador(n0,nf):
    primos = 0
    for num in range(n0,nf):
        if primo(num):
            primos += 1
    return primos 
        
n0 = int(input('INÍCIO: '))
nf = int(input('FIM: '))

qtd_primos = contador(n0,nf)
print("Primos = ",qtd_primos)