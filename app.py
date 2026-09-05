# Programa cálculo de médias
# Autor: Luiz Felipe 

# Entrada
nome = input("Digite o nome do aluno:\n")
nota1 = float(input("Dgite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))

# Processamento
media = (nota1 + nota2) / 2

# Saída
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 6:
    print("Situação: Aprovado")

else:
    print("Situação: Reprovado")