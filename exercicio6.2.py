def media_positivos(num,positivos):
    if positivos == 0:
        return 0
    media = sum(num)/positivos
    return media

num = []
positivos = 0
for _ in range(6):
    n = float(input())
    if n > 0:
        num.append(n)
        positivos += 1

resultado = media_positivos(num,positivos)

print()
print("Positivos =",positivos)
print("Média =",resultado)