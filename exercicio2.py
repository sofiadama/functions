def area(largura,comprimento):
    area_terreno = largura*comprimento    
    print(f"A área do terreno é igual a {area_terreno:.0f} m².")

l = float(input("Informe a largura (m): "))
c = float(input("Informe o comprimento (m): "))
    
area(l,c)