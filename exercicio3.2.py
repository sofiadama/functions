def inteiros(n):
    if n % 2 == 0:
        return "par"
    else:
        return "ímpar"
 
i = 0
pares = 0
impares = 0

while i < 10:
    n = int(input())
    paridade = inteiros(n)
    print("O número é",paridade)
    i += 1
    if paridade == "par":
        pares += 1
    if paridade == "ímpar":
        impares += 1
        
print()
print("Pares:",pares)
print("Ímpares:",impares)

