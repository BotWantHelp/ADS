class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def verificar_adulto(self):
        if self.idade >= 18:
            return f"{self.nome} é maior de idade."
        else:
            return f"{self.nome} ainda não é maior de idade."

pessoa1 = Pessoa("Alice", 25) # Criando uma instância da classe Pessoa
pessoa2 = Pessoa("Bob", 17)   # Criando outra instância da classe Pessoa

print(pessoa1.verificar_adulto())  # Verificando se a pessoa é maior de idade usando o método verificar_adulto
print(pessoa2.verificar_adulto())  

