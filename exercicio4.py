#Exercíco 2


menu = {
    100: {'produto': 'Cachorro Quente', 'preco': 1.20},
    101: {'produto': 'bauru simples ', 'preco': 1.30},
    102: {'produto': 'bauru com ovo', 'preco': 1.50},
    103: {'produto': 'hamburguer', 'preco': 1.20},
    104: {'produto': 'cheeseburguer', 'preco': 1.70},
    105: {'produto': 'Suco', 'preco': 2.20},
    106: {'produto': 'refrigerante', 'preco': 1.00},
}

codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo_produto in menu:
    produto = menu[codigo_produto]['produto']
    preco_unitario = menu[codigo_produto]['preco']

    valor_total = quantidade * preco_unitario

    print(f"O total a ser pago pelo {quantidade} {produto}(s) é R${valor_total:.2f}.")
else:
    print("Código do produto inválido.")
