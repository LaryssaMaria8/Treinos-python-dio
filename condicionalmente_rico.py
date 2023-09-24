saldo_total = int(input("Qual é o valor do saldo? "))
valor_saque = int(input("Quanto você deseja sacar? "))
if saldo_total >= valor_saque: 
 saldo_disponivel = saldo_total-valor_saque
 print("Seu saldo atual é de: ", saldo_disponivel)
else:
 print("Operação inválida! Valor de saque maior que o saldo")