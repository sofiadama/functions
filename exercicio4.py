def calcular_horario_chegada(h,t,f):
    horario_chegada = (h + t + f) % 24
    print(horario_chegada)
    
h,t,f = map(int,input().split())
#converter str para int

calcular_horario_chegada(h,t,f)
