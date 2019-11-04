#Dicionários são criados colocando os pares chave: valor entre chaves { } das seguinte forma:


di = {‘Julio’: ‘C’, ‘Jaime’: ‘Python’, ‘Ana’: ‘Ruby’, ‘Claudia’: ‘Java’, ‘Mauro’: ‘PHP’}

#LISTA DE TUPLAS
di = dict([(‘Julio’, ‘C’), (‘Jaime’, ‘Python’), (‘Ana’, ‘Ruby’), (‘Claudia’, ‘Java’), (‘Mauro’, ‘PHP’)])
di['Ana']
#Dicionário em branco
di = {}

#Percorendo dicionário com for
linguagens =  {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Cláudia': 'Java', 'Mauro': 'PHP'}
for chave in linguagens:
    print(chave, 'programa em:', linguagens[chave])

#Alterando um valor no dicionario
di = {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Cláudia': 'Java', 'Mauro': 'PHP'}
di['Jaime'] = 'PHP'
print(di)

#Inserindo um item em um dicionário
di = {'Portugal': 'Lisboa', 'Espanha': 'Madri', 'Itália': 'Roma'}
print(di)

di['França'] = 'Paris'
print(di)

#Inserindo itens ou alterando itens em um dicionário com o método update()
di = {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Cláudia': 'Java', 'Mauro': 'PHP'}
print(di)
di.update({'Paulo': 'C++', 'Mauro': 'Swift'})
print(di)

#Removendo um par chave, valor de um dicionário usando o comando del
di = {'Claudia': 'Java', 'Jaime': 'Python', 'Julio': 'C', 'Mauro': 'PHP', 'Ana': 'Ruby'}
del di['Mauro']
print(di)
