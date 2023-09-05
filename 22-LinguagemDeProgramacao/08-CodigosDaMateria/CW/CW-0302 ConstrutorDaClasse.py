''' o método construtor é chamado de __init__() e deve ser usado conforme o código a seguir. 
 Na classe FuncionarioTecnico, o atributo status, que é uma variável de instância, 
 recebe o valor no momento da criação do objeto, pois está no construtor.'''

class FuncionarioTecnico:
    def __init__(self, nivel, status):
        self.nivel = nivel
        self.status = status

nivel = 'Técnico'
func1 = FuncionarioTecnico(nivel, 'Ativo')
func2 = FuncionarioTecnico(nivel, 'Licença Mestrado')

print(func1.nivel)
print(func2.nivel)
print(func1.status)
print(func2.status)

''' Todo método em uma classe deve receber como primeiro parâmetro uma variável 
 que indica a referência à classe, por convenção, adota-se o parâmetro self. 
 O parâmetro self será usado para acessar os atributos e métodos dentro da própria classe.'''