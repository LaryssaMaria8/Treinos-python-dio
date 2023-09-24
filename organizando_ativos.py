ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Digite o número de ativos que você deseja organizar: "))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input("Digite o ativo: ")
    ativos.append(codigoAtivo)
    
    ativos.sort()
    for ativo in ativos:
      print (ativo)
