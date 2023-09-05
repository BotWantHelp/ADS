class Pessoa:
    def __init__(self, nome, idade, genero):       # tambem conhecido como contrutor
        self.nome = nome                           # aqui se passa todos os atributos da classe
        self.idade = idade
        self.genero = genero
                
    def verificar_adulto(self): # função para verificar se é adulto ou não
        if self.idade >= 18:
            return f"{self.nome} é maior de idade."
        else:
            return f"{self.nome} ainda não é maior de idade."

    def ver_oficio(self):     # função para ver o oficio da pessoa
        if self.idade >= 18 and self.genero == "masculino":
            return f"{self.nome} é {self.genero} e trabalha com Programação"
        elif self.idade >= 18 and self.genero == "feminino":
            return f"{self.nome} é {self.genero} e trabalha com Designer"
        else:
            return f"{self.nome} é {self.genero} e é estudante"
    
pessoa1 = Pessoa("Alice", 25, 'feminino')  # Criando uma instância da classe Pessoa
pessoa2 = Pessoa("Bob", 15, "masculino")   # Criando outra instância da classe Pessoa
pessoa3 = Pessoa("Pedro", 35, "masculino")  # Criando outra instância da classe Pessoa

print(pessoa1.verificar_adulto())  # Verificando se a pessoa é maior de idade usando o método verificar_adulto
print(pessoa2.verificar_adulto())  # Verificando se a pessoa é maior de idade usando o método verificar_adulto
print(pessoa3.ver_oficio())        # Verificando se a pessoa é maior de idade se estuda ou trabalha
