import json #importei o arquivo json (no caso: dados.json)

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)
print(dados['nome'])

#convertendo json em str
texto =  json.dumps(dados, indent=4, ensure_ascii=False) #dumps faz a conversão 
print(texto)

#convertendo o str em json
pessoaNova = '{"primeironome":"Vânia", "idade": 50}'

dadosNovo = json.loads(pessoaNova)
print(dadosNovo)

#atualizando
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

dados['idade'] = 36 #alteração
dados['redesocial'] = "kau.tech" #adicionando um dado
del dados['telefone'] #deletando um dado

#'w' = write ~ escrever
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dado adicionado com sucesso!")
print("Telefone removido com sucesso!")
print(dados)