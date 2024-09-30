def quad(X,Y):
    i = 0
    while i < 4:
        i += 1
        if X > 0 and Y > 0:
            print("primeiro")
        elif X < 0 and Y > 0:
            print("segundo")
        elif X < 0 and Y < 0:
            print("terceiro")
        elif X > 0 and Y < 0:
            print("quarto")
        else:
            break
        
        X = int(input('X: '))
        Y = int(input('Y: '))
        
X = int(input('X: '))
Y = int(input('Y: '))

quad(X,Y)