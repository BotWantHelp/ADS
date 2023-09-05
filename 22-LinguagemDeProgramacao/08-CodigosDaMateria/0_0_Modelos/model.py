class minhaCasa: #"class" para indicar a criação de uma classe, seguida do nome e de dois pontos
    altura = None      # No bloco indentado devem ser implementados os atributos e métodos da classe.
     
    def corParede(self, cor):
         self.cor = cor
    def quartos(self, quarto):
         self.quarto = quarto

# Os atributos e os métodos de uma classe podem ser acessados pelo objeto, 
# colocando o nome deste seguido de ponto; 

objeto1 = minhaCasa()
objeto1.cor = "cobre"
objeto1.quarto = 1
 
print(objeto1.cor)
