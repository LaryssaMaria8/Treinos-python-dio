texto = input("Digite um texto")
Deve_conter = ABCD

for letra in texto:
    if letra.upper() in Deve_conter:
    print(letra)
    print()
