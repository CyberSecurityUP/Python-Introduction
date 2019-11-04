#Problema: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
         # como parâmetro e mostre uma mensagem com o tamanho adaptável.
# Função para imprimir mensagens dentro de cabeçalho com bordas
def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}  ')
    print('-' * (len(mensagem) + 4))


# Cases de chamada da função
escreva('Olá, mundo')
escreva('Python é a melhor linguagem do mundo')
escreva('Python é maior que Java')


#Problema: Faça um programa que tenha uma função chamada area(), que receba as dimeções
         # de um terreno retangular(largura e comprimento) e mostre a área do terreno.
#Função para impressão de cabeçalho
def header(mensagem):
    print('-' * 30)
    print(f'{mensagem:^30}')
    print('-' * 30)


# Função para calcular area do terreno
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {area}m²')


header('Área de Terreno')
larg = float(input('Largura em (m): '))
compri = float(input('Comprimento em (m): '))

area(larg, compri)
