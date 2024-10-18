def ajuste_salarial(salario):
    faixas = [(2000, 0.04),(1200, 0.07),(800, 0.10),(400, 0.12),(0, 0.15)]
    
    for limite, percentual in faixas:
        if salario > limite:
            aumento = salario * percentual
            novo_salario = salario + aumento
            break
    
    print()
    print(f"Novo salário: R$ {novo_salario:.2f}")
    print(f"Reajuste de: R$ {aumento:.2f}")
    print(f"Em percentual: {percentual*100:.0f}%")

salario = float(input("Informe seu salário: R$ "))
ajuste_salarial(salario)
