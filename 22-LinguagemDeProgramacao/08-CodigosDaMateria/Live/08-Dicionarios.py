# Também sao conhecidos como mapa, uma coleção de elementos,
# no qual temos N entradas associadas a uma ou mais chaves por entrada.

             #  Chave : Valor
dicionario = { 'nome' : 'rapha',    # Chave Nome, Valor Rapha
               'idade': '51',      # Chave Idade, Valor 51
               'sexo' : 'feminino'} # Chave Sexo, Valor Feminino

print("Dicionário original:")
print(dicionario,'\n')

dicionario['nome'] = 'Raiana' # Alterando o valor da chave 'chave_nome'
print(dicionario,'\n')   # Print do novo valor de 'chave_nome'

dicionario['sexo'] = 'masculino' # Alterando o valor da chave 'chave_sexo'
print(dicionario,'\n')   # Print do dicionário após alteração de sexo pelo SUS

novo_registro = {   # podemos aicionar um novo registro ao dicionario
    'nome': 'João',
    'idade': 30,
    'sexo': 'masculino'
}

dicionario['novo_registro'] = novo_registro  # Adicionando ao dicionário o novo registro
print(dicionario)  # Print do dicionário após adicionar o novo registro


