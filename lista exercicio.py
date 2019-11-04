valores = [[], []]  # indice 0 corresponde a valores pares, já o 1 a valores ímpares --> [[PARES], [ÍMPARES]]

for cont in range(7):
    numero = int(input(f'Informe o {cont + 1}º número: '))

    # Verifica qual é par e qual é ímpar e distribui em suas respectivas listas
    if numero % 2 == 0:
        valores[0].append(numero) #LISTA1
    else:
        valores[1].append(numero) #LISTA2

valores[0].sort()  # Ordena valores pares em ordem crescente
valores[1].sort()  # Ordena valores ímpares em ordem crescente

print('-' * 40)
print(f'TODOS VALORES: {valores}')
print(f'\nVALORES PARES DIGITADOS: {valores[0]}')
print(f'VALORES ÍMPARES DIGITADOS: {valores[1]}')
