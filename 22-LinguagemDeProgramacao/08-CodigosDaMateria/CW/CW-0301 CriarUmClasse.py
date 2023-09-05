# Para criar uma classe em Python é necessária a sintaxe a seguir. 

class PrimeiraClasse: #"class" para indicar a criação de uma classe, seguida do nome e de dois pontos
     nome = None      # No bloco indentado devem ser implementados os atributos e métodos da classe.
     
     def imprimir_mensagem(self, mensagem):
         self.mensagem = mensagem
         print(mensagem)

# Os atributos e os métodos de uma classe podem ser acessados pelo objeto, 
# colocando o nome deste seguido de ponto; 

objeto1 = PrimeiraClasse()
objeto1.nome = "Aluno 1"
 
print(objeto1.nome)
objeto1.imprimir_mensagem(mensagem = "Seja bem vindo")
