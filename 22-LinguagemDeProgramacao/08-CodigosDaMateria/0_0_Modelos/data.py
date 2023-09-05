import datetime as dt

# Operações com data e hora
hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)
uma_semana_atras = hoje - dt.timedelta(weeks=1)

agora = dt.datetime.now()
duas_horas_atras = agora - dt.timedelta(hours=2)

# Formatação
hoje_formatado = dt.datetime.strftime(hoje, "%d-%m-%Y") #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
ontem_formatado = dt.datetime.strftime(ontem, "%d de %B de %Y")

# Converção de string para data
data_string = '11/06/2019 15:30'
data_dt = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatado)
print(ontem)
print(ontem_formatado)