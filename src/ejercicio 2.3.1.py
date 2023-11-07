Edad=int(input("¿cual es tu edad?: "))

while Edad== None:
    try:
        Edad=int(input("¿cual es tu edad?: "))
    except ValueError:
        print("Por favor, dame un número")

Edad==1
if Edad<1: 
    print ("error")
else:
    for i in range(0,Edad): 
        print(i+1)




