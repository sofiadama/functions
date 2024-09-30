def contador(Z,X):
    inteiros = 1
    while Z <= X:
        Z = int(input('Z: '))
    if Z > X:
        inteiros += 1
    print(inteiros)

X = int(input('X: '))
Z = int(input('Z: '))
      
contador(Z,X)