import pandas as pd
from IPython.display import display

# Criar um DataFrame de exemplo
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 22, 28],
        'Cidade': ['São Paulo', 'Nova Iorque', 'Londres', 'Toronto']}

df = pd.DataFrame(data)

print("\nUsando a função print() para mostrar o DataFrame\n")
print(df)

print("\nUsando a função display() para mostrar o DataFrame\n")
display(df)
