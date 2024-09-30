def ajuste(salario):
    if salario <= 400:
        novo_salario = salario + salario*0.15
        aumento = salario*0.15
        percentual = 15
    elif salario <= 800:
        novo_salario = salario + salario*0.12
        aumento = salario*0.12
        percentual = 12
    elif salario <= 1200:
        novo_salario = salario + salario*0.10
        aumento = salario*0.10
        percentual = 10
    elif salario <= 2000:
        novo_salario = salario + salario*0.07
        aumento = salario*0.07
        percentual = 7
    elif salario > 2000:
        novo_salario = salario + salario*0.04
        aumento = salario*0.04
        percentual = 4

    print(f"Novo salário: R$ {novo_salario:.2f}")
    print(f"Reajuste de: R$ {aumento:.2f}")
    print(f"Em percentual: {percentual} %")
        
salario = float(input("Informe seu salário: R$ "))

ajuste(salario)