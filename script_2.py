#Aquecimento
#questao 1
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
tamanho_lista = len(lista)
menor_valor = min(lista)
maior_valor = max(lista)
soma_valoes = sum(lista)

print(f"A lista possui {tamanho_lista} números em que o maior é {maior_valor} e o menor é {menor_valor}")

#questao 2: tabuada

numeros_1_a_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def tabuada(n):
    string_tabuada = f"Tabuada do {n}:"
    for x in numeros_1_a_10: 
        str_linha = f"\n{n} x {x} = {n*x}"
        string_tabuada += str_linha
    print(string_tabuada)

numero_usuario = int(input("Digite um número: "))
tabuada(numero_usuario)

#questao 3: lista filotrada por nmumeros de 3
#aqui provavelmente é bom usar filter

lista_2 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

mult_3 = list(filter(lambda x: x % 3 == 0, lista_2))
print(mult_3)

#questao 4: elevando numeros ao quadrado

lista_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_quadrados = list(map(lambda x: x**2, lista_3))
print(lista_quadrados)

#questao 5:

nota_1 = int(input("Digite o valor da primeira nota: "))
nota_2 = int(input("Digite o valor da segunda nota: "))
nota_3 = int(input("Digite o valor da terceira nota: "))
nota_4 = int(input("Digite o valor da quarta nota: "))
nota_5 = int(input("Digite o valor da quinta nota: "))

lista_notas = [nota_1, nota_2, nota_3, nota_4, nota_5]

def calc_pontuacao(notas) -> float:
    notas.remove(max(notas))
    notas.remove(min(notas))

    soma_notas = sum(notas)
    media = soma_notas/3

    return media

print(f"Nota da manobra: {calc_pontuacao(lista_notas)}")