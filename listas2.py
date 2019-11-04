#AGORA VAMOS VER MÉTODOS PARA INCLUIR E REMOVER EM UMA LISTA

#PRIMEIRO METODO .APPEND QUE TEM COMO OBJETIVO ADICIONAL ALGO NO FINAL DA LISTA

livros = ['Java','SqlServer', 'Delphi','Python']
livros.append('Android')
print(livros)

#Entrada de dados
livros.append(input("digite: "))
print(livros)

#Caso deseje inserir em uma posição especifica sendo na primeira coluna ou última
#utilize o insert

livros = ['Java', 'SqlServer', 'Delphi', 'Python', 'Android']
livros.insert(0,'Oracle')
livros

#Entrada de dados
livros.insert(0,input("Digite: "))
print(livros)

#Remover o último item da lista e o retorna como resultado da operação
livros = ['Java', 'SqlServer', 'Delphi', 'Python', 'Android']
livros.pop()
livros.pop(1)
livros.pop(2)
print(livros)

#Remover um determinado valor
livros.remove('Oracle')
print(livros)

#Outros métodos muito importantes ao trabalhar com listas são o sort(), que ordena a lista, e o reverse()
livros.reverse()
print(livros)

livros.sort()
print(livros)

#Temos o count que retorna quantos informações repetem na lista
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Oracle']
livros.count('Python')
livros.count('Oracle')
