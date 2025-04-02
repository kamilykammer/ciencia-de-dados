# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido) 
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():

    # Definição dos grupos e valores
    grupos = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']
    valores = [3500, 4200, 3900, 4800, 4500, 5000, ]

    # Configura um grśfico de barras, onde recebe os grupos, valores
    # E opcionalmente ass cores]
    plt.bar(grupos, valores, color=['lightblue', 'lightgreen', 'lightcoral', 'lightgray', 'lightpink', 'lightyellow'])

    # Define o título do gráfico
    plt.title('Trafego do site po mês (Visitas)')

    # Define o título do eixo X
    plt.xlabel('Mês')

    # Define o título do eixo Y
    plt.ylabel('Visitas')

    # Cria o gráfico
    plt.show()

    # Salva dentro do arquivo de imagem
    plt.savefig('chart.png')