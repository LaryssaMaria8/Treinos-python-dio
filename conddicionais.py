Saque = float(input("Qual valor você deseja sacar "))
Conta_normal = 2800
Conta_estudantil = 8880
Cheque_especial = 2200

if Saque <= Conta_normal:
    print("Saque realizado com sucesso")

elif Saque <= (Conta_normal+Conta_estudantil):
    print("Saque realizado com sucesso utilizando o cheque especial")

else:
    print("Ação invalida! Saldo indisponivel")
