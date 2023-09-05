import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame de exemplo
data = {'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Vendas': [100, 150, 200, 120, 180, 250]}

df = pd.DataFrame(data)

# Criar um gráfico de linhas usando Matplotlib
plt.figure(figsize=(8, 5))  # Definir o tamanho da figura

plt.plot(df['Mês'], df['Vendas'], marker='o')  # Plotar os dados com marcadores 'o'
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas')

plt.grid(True)  # Adicionar uma grade
plt.show()  # Mostrar o gráfico
