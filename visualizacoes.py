import matplotlib.pyplot as plt

def plot_valor_categoria(valor_categoria):
    valor_categoria.plot(kind='bar', title='Valor em Estoque por Categoria', ylabel='R$')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_fornecedores(compras, fornecedores):
    compras_fornecedores = compras.merge(fornecedores, on='FornecedorID')
    participacao = compras_fornecedores.groupby('Nome')['PrecoCompra'].sum()
    participacao.plot(kind='pie', autopct='%1.1f%%', title='Participação dos Fornecedores')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
