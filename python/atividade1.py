#Respostas exercicios
print('Código atividade 1: Help Desk')

nome_do_cliente = input('Informe o nome:')
descricao_do_problema = input('Descreva o problema:')
numero_ticket = input('Qual o número do ticket?:')

print(numero_ticket)
print ((type(int(numero_ticket))))

print('Boas-vindas' , nome_do_cliente.upper())
print('Quantidade de caracteres existente neste problema:' , (len(descricao_do_problema)))
#não sei se converti o numero_ticket no local certo
#mensagem de boas vindas não sei se isso que fiz seria interpolação.
print('Código atividade 2: Alimentos e Bebidas')

nome_drink_prato = input('Qual o nome do Drink/Prato?')
quantidade_padrao = input('Qual a quantidade padrão de ml/gramas do ingrediente principal por porção?:')
quantidade_pessoas = input('Qual a quantidade de pessoas que serão servidas?:')
calculo_ingrediente = int(quantidade_pessoas) * int(quantidade_padrao)

print (float(quantidade_padrao))
print (int(quantidade_pessoas))
print ('A quantidade necessária de ingredientes:' ,  calculo_ingrediente)
