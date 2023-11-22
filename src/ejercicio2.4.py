arreglo
def ord_burbuja(arreglo):
    n=len(arreglo)

for i in range(n-1):
    for j in range(n-1-i):
        if arreglo[j]> arreglo[j+1]:
            arreglo[j], arreglo[j+1]= arreglo[j+1], a[j]

a = [8, 3, 1, 19, 14]
ord_burbuja(a)

print(a)