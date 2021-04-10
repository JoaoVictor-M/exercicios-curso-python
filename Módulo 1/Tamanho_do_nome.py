#Tamanho do nome
nome = input("Digite seu primeiro nome: ")

#Pega a quantidade de caracteres da string 
qt = len(nome)

if qt <= 4:
    print("Seu nome é curto")

elif qt <= 6:
    print("Seu nome é normal")

else:
    print("Seu nome é grande")