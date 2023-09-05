import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)                    # Exemplo de gráfico de linha
y = np.sin(x)
plt.plot(x, y)
plt.title("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

x = np.random.rand(50)                         # Exemplo de gráfico de dispersão (scatter plot)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Gráfico de Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

categorias = ['A', 'B', 'C', 'D']              # Exemplo de gráfico de barras
valores = [15, 8, 12, 6]
plt.bar(categorias, valores)
plt.title("Gráfico de Barras")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.show()

labels = ['Gordo', 'Feio', 'Olheiras']         # Exemplo de gráfico de pizza
sizes = [50, 20, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("Gráfico de Pizza")
plt.show()

dados = np.random.randn(1000)                  # Exemplo de gráfico de histograma
plt.hist(dados, bins=20, edgecolor='black')
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()
