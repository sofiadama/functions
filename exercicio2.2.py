def calculo_media_e_melhor_nota(notas):
    media = sum(notas) / len(notas)
    melhor_nota = max(notas)
    return media, melhor_nota

notas = []
for i in range(5):
    nota = float(input("Nota: "))
    notas.append(nota)

media, melhor_nota = calculo_media_e_melhor_nota(notas)

print(f"A média da turma é: {media:.2f}")
print(f"A melhor nota é: {melhor_nota:.2f}")

if media >= 5.75:
    print("Status do aluno: Aprovado")
elif media >= 2.75:
    print("Status do aluno: Em recuperação")
else:
    print("Status do aluno: Reprovado")