import matplotlib, random, math
import numpy as np
print(matplotlib.__version__)
print("Hello World")
#questao 3
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

numero_escolhido = random.choice(lista)
#questao 4

val_menorque_100 = random.randrange(100)
print(f"valor menor  que 100 gerado: {val_menorque_100}")
'''
randrange escolhe aleatoriamente um valor em um range de 0 ate
(mas nao incluindo), o valor informado.
'''
#questao 5
base = float(input("Digite um valor para a base: "))
expoente = int(input("Digite um valor par o expoente: "))
resultado = math.pow(base, expoente)

print(f"O resultado é: {resultado:.2f}!!")

#questao 6

numero_participantes = int(input("Quantos participarão do sorteio?: "))
numero_sorteado = random.randrange(numero_participantes + 1)
print(f"O participante escohido foi o número {numero_sorteado}")

#questao 7 

nome_usuario = str(input("Informe seu nome: "))
token_gerado = random.randrange(1000, 9999, 2)

print(f"Olá {nome_usuario}! O seu token de acesso é {token_gerado}. Seja bem vindo(a)")

#questao 8

frutas = ["maçã", "banana", "uva", "pêra", 

          "manga", "coco", "melancia", "mamão",

          "laranja", "abacaxi", "kiwi", "ameixa"]

fruta_escolhida = random.sample(frutas, 3) #sample nao escolhe elementos iguais, serao 3 diferentes


