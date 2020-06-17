l = [6,9,2,4,7,1,8]
print('Lista ingresada:\n', l)

def metodoBurbuja(l):
    for i in range (1, len(l)):
        for j in range(0, len(l)-i):
            if(l[j+1] < l[j]):
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
    print('Lista con el metodo de la burbuja:\n', l)

def metodoSort(l):
    l.sort()
    print('Lista con el metodo Sort:\n', l)

metodoBurbuja(l)
metodoSort(l)

