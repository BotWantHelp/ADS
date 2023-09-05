#Dicionários: As estruturas de dados que possuem um mapeamento entre 
# uma chave e um valor são consideradas objetos do tipo mapping. 
# Em Python, o objeto que possui essa propriedade é o dict (dicionário). 
# Tal objeto é mutável, ou seja, com ele conseguimos atribuir 
# um novo valor a uma chave já existente.

# Em Python, uma das maneiras de criar um objeto do tipo dicionário é colocando as chaves e os valores entre estas, conforme código a seguir:
cadastro = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print(cadastro)             # Mostra o dicionario completo

print(cadastro['nome'])     # Mostra um valor do dicionario
                            # nome_dicionario[chave] = novo_valor
                            
cadastro['nome'] = 'Rapha'  # Atribuir um novo valor, em nome
print(cadastro)             # Como fica depois da alteração
