# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O dobro de {} é {}\nO triplo é {} \nE a raíz quadrada é {}'.format(n,dobro, triplo, raiz))