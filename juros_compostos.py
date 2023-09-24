valor_inicial = float(input("Qual é o valor do seu investimento? "))
taxa_juros = float(input("Qual é a taxa do seu juros? "))
periodo = int(input("Quanto tempo você levará para pagar? "))

valor_final = valor_inicial * (1+taxa_juros) ** periodo
valor_final = round(valor_final, 2)


print(f"Valor final do investimento: R$ {valor_final:.2f}")