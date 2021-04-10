#Ficha + IMC
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

print(f"\n{nome} tem {idade} anos, pesa {peso}kg e mede {altura:.2f} de altura.\nSeu IMC é {imc:.2f}.")