def pediredad ():
    salir = False
    while not salir:
        try:
            Edad=int(input("¿cual es tu edad?: "))
            salir = True
        except ValueError:
            print("Por favor, dame un número")


if Edad<1: 
    print ("error")
else:
    for i in range(0,Edad): 
        print(i+1)




