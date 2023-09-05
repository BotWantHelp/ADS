from datetime import datetime, timedelta

# Obtendo a data e hora atual
data_atual = datetime.now()
print("Data e Hora Atual:", data_atual)

# Criando uma data específica
data_especifica = datetime(2023, 8, 13, 15, 30, 0)
print("Data Específica:", data_especifica)

# Obtendo partes individuais da data
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day
hora = data_atual.hour
minuto = data_atual.minute
segundo = data_atual.second
print("Ano:", ano)
print("Mês:", mes)
print("Dia:", dia)
print("Hora:", hora)
print("Minuto:", minuto)
print("Segundo:", segundo)

# Formatando datas como strings
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print("Data Formatada:", data_formatada)

# Realizando cálculos com datas
outra_data = data_atual + timedelta(days=7, hours=3)
print("Data Atual + 7 dias e 3 horas:", outra_data)

# Calculando a diferença entre datas
diferenca = outra_data - data_atual
print("Diferença de Tempo:", diferenca)
print("Diferença em Dias:", diferenca.days)
print("Diferença em Segundos:", diferenca.total_seconds())