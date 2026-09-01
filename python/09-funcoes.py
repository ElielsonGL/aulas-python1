#Função - void    ~ vazia ()
def saudacao():
    print("Olá, tudo bem?")

#acessando a função
saudacao()

#Função com parâmetro
def saudacao(nome):
    print("Olá,", nome)

#Acessando a Função
saudacao("João")

#função de retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

#Exemplo com tratamento de erro
try: #tentar
    numero = int(input("Digite um número: "))
    print(numero)
except: #caso não consiga
    print("Você digitou algo inválido!")

#Try e Except usando Else e Finally juntos
try:
    numero = float(input("Digite um NOVO número:"))
except ValueError: #ValueError 
    print("Erro: entrada inválida")
else:
    print("Você digitou:" ,  numero)
finally: #finaliza um programa, existindo exceção ou não.
    print("Programa finalizado")

#exemplo de função com try e except
def dividir(a, b):
    try:
        return a/ b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

print(dividir(10, 2))
print(dividir(23, 0))

#entrada do usuário
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo numero: "))
print(dividir(a, b))