def media_idades(idades):
    media = sum(idades) / len(idades)
    return media

idades = []
i = 0
while i >= 0:
    idade = int(input('Idade: '))
    if idade < 0:
        break
    idades.append(idade)


media = media_idades(idades)
print(f"{media:.2f}")
