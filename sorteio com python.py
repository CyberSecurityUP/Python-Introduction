import random #importamos a biblioteca Random ( que em inglês significa aleatório) , vai nos proporcionar o essencial dessa aplicação o sorteio (vamos ver melhor mais adiante)


j1 = input('(1° jogador) Digite seu nome: ')#2
j2 = input('(2° jogador) Digite seu nome: ')#3
j2 = input('(3° jogador) Digite seu nome: ')#4

sort = random.randint(1,10) # Sortear um numero de 1 a 3

if sort == 1:
    print('Parabéns',j1,'Você Ganhou!!')
elif sort == 3:
    print('Parabéns',j2,'Você Ganhou!!')
elif sort == 5:
    print('Parabéns',j3,'Você Ganhou!!')
else:
    print("Ninguém ganhou")
