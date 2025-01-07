# Conversor de Moedas Eu/US
valor = float(input('quanto dinheiro em R$ você tem na carteira? '))
dolar = valor/6.15
euro = valor/6.32

print('com o valor de R${} da para comprar {:.2f} dolares'.format(valor, dolar))
print('com o valor de R${} da para comprar {:.2f} euros'.format(valor, euro))