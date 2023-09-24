valor = float(input("Quanto você deseja depositar? "))

if valor > 0:
    print(f"depósito realizado com sucesso! O valor atual é de R${valor:.2f}")
elif valor == 0:
  print("Encerrando o programa...")
else:
  print("Ação inválida! Digite um valor positivo")
