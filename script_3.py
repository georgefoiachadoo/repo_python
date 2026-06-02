#aquecimento
#questao 1: soma dos elementos de uma lista de listas
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma_elementos = [sum(el) for el in lista_de_listas]
print("1) ", soma_elementos)

#questao 2: lista de terceiros elementos de tuplas em listas

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista_3_elementos = [el[2] for el in lista_de_tuplas]
print("2) ", lista_3_elementos)

#questao 3: lista de tuplas

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tuplas_1 = [(lista.index(el), el) for el in lista]

print("3) ", lista_tuplas_1)

#questao 4: listas com listcomprehension

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
lista_apartamentos = [item[1] for item in aluguel if item[0] == 'Apartamento']
print("4) ", lista_apartamentos)

#questao 5: dicionarios com dict comprehension

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dict_1 = {meses[i]:despesa[i] for i in range(len(meses))}

print("5) ", dict_1)

#questao 6: loja, list comprehension

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

lista_2022_6000  = [(item[0], item[1]) for item in vendas if item[0] == '2022' and item[1] > 6000]

print("6) ", lista_2022_6000)

#questao 7: cinica, lista de tuplas
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

lista_tuplas_2 = [
    ("Hipoglicemia", valor) if valor <= 70 
    else ("Normal", valor) if valor <= 99
    else("Alterada", valor) if valor <=125
    else("Diabetes", valor)
    for valor in glicemia
    ]

print("7) ", lista_tuplas_2)

#questao 8: e-commerce

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

cabecalho = [("ID", "QUANTIDADE", "PRECO", "TOTAL")]
itens_tabela = [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
tabela = cabecalho + itens_tabela

print("8) ", tabela)