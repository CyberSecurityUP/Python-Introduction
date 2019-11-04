lista = ['O carro','peixe',123,111,True]
lista
print(lista)

nova_lista = ['pedra',lista]

#ACESSANDO ELEMENTOS UTILIZANDO SINTAXE E INDICE
lista[0]
lista[1]
lista[2]
lista[3]
lista[4]

nova_lista[0]
nova_lista[1][2]

#COmprimento de uma lista
len(lista)
len(nova_lista)

#Ajuntar e repetir lista
lista+nova_lista
lista*3

#Verificando a existência de uma informação dentro de uma lista
'peixe' in lista
'gato' in lista
'felipe' in lista

#Encontrar os menores valores, maiores valores e somar
numeros = [14.55, 67, 89.88, 10, 21.5]
min(numeros)
max(numeros)
sum(numeros)
