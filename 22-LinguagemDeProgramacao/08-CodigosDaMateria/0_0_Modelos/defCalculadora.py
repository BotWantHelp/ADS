class calculadora(object):
    
    def _init_(self, somar):
        self.somar = somar
  
    def somar(self, a, b):
        return a + b 

calculo = calculadora()
i = calculo.somar(50, 60)


print(f'o resultado do método invocado é:.... {i}')
