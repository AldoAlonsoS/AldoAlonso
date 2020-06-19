import re
print('\nValidacion de Correos\n')
Listacorreos = ('juan@padts.mx', 'juan@padts.com.mx', 'juan@python.padts.mx', 'chi vas@344.12', 'chivas12@gmail_com')

verifica = '[\w\d\._-]+@[A-Za-z]+\.[A-Za-z]+(\.[A-Za-z])*'

for i in Listacorreos:
    print(f'{i} ==> Correo valido' if re.match(verifica, i) else f'{i} ==> Correo Invalido')

print('\nValidacion de Numeros\n')

numerosTelefonicos = ('9711900640', '(971)1900640', '(55)1233445', '(55) 123 5678', '(55) 123-4567', '(3456)234-345', '(234)_234 6789')

valida = '\(*\d{2,3}\)*[\s-]*\d{2,3}[\s-]*(\d{4})$'    #'\(*\d{2,10}\)*\d{7,8}' bueno 3 numeros     #'[\d{10}\(\)]\(\d{2,3}\)'

for i in numerosTelefonicos:
    print(f'{i} ==> Numero valido' if re.match(valida, i)else f'{i} ==> Numero invalido')


#Listacorreos2 = ('aldo-alonso18@gmail.com', 'jc.alonso.sanchez.23@gmail.com', 'carlos_alonso06@hotmail.com')

#verificaDominio = '.+@[A-Za-z]+'
#for i in Listacorreos2:
 #   print(f'{i} ==> Dominio Valido' if re.match(verificaDominio, i) else f'{i} ==> Dominio Invalido')









