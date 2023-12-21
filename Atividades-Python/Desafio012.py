preço=float(input('Qual o preço do produto? R$ '))
np=preço-(preço*5/100)
print(f'O novo preço do produto com 5% de desconto será de R${np:.2f}')
