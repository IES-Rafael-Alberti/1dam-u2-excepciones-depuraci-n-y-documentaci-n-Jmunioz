def pediredad ():
    salir = False
    while not salir:
        try:
            Edad=int(input("¿cual es tu edad?: "))
            salir = True
        except ValueError:
            print("Por favor, dame un número")

    return Edad

def edadcont(Edad):
    if Edad<1: 
        print ("error")
    else:
        for i in range(0,Edad): 
            print(i+1)

def main():
    edad = pediredad()
    edadcont(edad)

if __name__ == "__main__":
    main()


