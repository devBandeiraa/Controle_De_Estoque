import pandas as pd

def movimentacoes_por_produto(movs, produtos):
    """
    Retorna um DataFrame com as quantidades de entrada e saída por produto.
    """
    agrupado = movs.groupby(['ProdutoID', 'TipoMov'])['Quantidade'].sum().unstack(fill_value=0)
    agrupado.columns = ['Entrada', 'Saida']
    agrupado = agrupado.reset_index().merge(produtos[['ProdutoID', 'Nome']], on='ProdutoID')
    return agrupado[['Nome', 'Entrada', 'Saida']]


def valor_estoque_por_categoria(produtos, categorias):
    df = produtos.merge(categorias, on='CategoriaID')
    df['ValorEstoque'] = df['PrecoUnitario'] * df['EstoqueAtual']
    resultado = df.groupby('NomeCategoria')['ValorEstoque'].sum().reset_index()
    resultado.rename(columns={
        'NomeCategoria': 'Categoria',
        'ValorEstoque': 'Valor Total (R$)'
    }, inplace=True)
    return resultado


def produtos_extremos(produtos):
    """
    Retorna os produtos com maior e menor valor total em estoque.
    """
    produtos['ValorTotalEstoque'] = produtos['PrecoUnitario'] * produtos['EstoqueAtual']
    maior = produtos.loc[produtos['ValorTotalEstoque'].idxmax()]
    menor = produtos.loc[produtos['ValorTotalEstoque'].idxmin()]
    return maior, menor


def movimentacoes_mensais(movs):
    """
    Retorna um DataFrame com movimentações agrupadas por mês.
    """
    movs['AnoMes'] = pd.to_datetime(movs['DataMov']).dt.to_period('M')
    resultado = movs.groupby(['AnoMes', 'TipoMov'])['Quantidade'].sum().unstack(fill_value=0).reset_index()
    resultado.columns.name = None
    return resultado


def movimentacoes_por_usuario(movs, usuarios):
    """
    Retorna a soma de movimentações feitas por cada usuário.
    """
    movs_usuarios = movs.groupby('UsuarioID')['Quantidade'].sum().reset_index()
    resultado = movs_usuarios.merge(usuarios, on='UsuarioID')
    return resultado.sort_values(by='Quantidade', ascending=False)
