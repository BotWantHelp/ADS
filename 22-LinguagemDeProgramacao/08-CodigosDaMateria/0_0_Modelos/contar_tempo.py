
from datetime import datetime, timedelta

valor_inicial = datetime.now()
print(valor_inicial)

i = 0

for i in range(1000000):
    i = i + 1

valor_final = datetime.now()
print(valor_final)

tempo_decorrido = valor_final - valor_inicial

print("Demorou:", tempo_decorrido)
print("Valor:", i)





