import pandas as pd

def movimentacoes_por_produto(movs, produtos):
    agrupado = movs.groupby(['ProdutoID', 'TipoMov'])['Quantidade'].sum().unstack(fill_value=0)
    agrupado.columns = ['Entrada', 'Saida']
    agrupado = agrupado.reset_index().merge(produtos[['ProdutoID', 'Nome']], on='ProdutoID')
    return agrupado[['Nome', 'Entrada', 'Saida']]

def valor_estoque_por_categoria(produtos, categorias):
    df = produtos.merge(categorias, on='CategoriaID')
    df['ValorEstoque'] = df['PrecoUnitario'] * df['EstoqueAtual']
    return df.groupby('NomeCategoria')['ValorEstoque'].sum().sort_values(ascending=False)

def produtos_extremos(produtos):
    produtos['ValorTotalEstoque'] = produtos['PrecoUnitario'] * produtos['EstoqueAtual']
    maior = produtos.loc[produtos['ValorTotalEstoque'].idxmax()]
    menor = produtos.loc[produtos['ValorTotalEstoque'].idxmin()]
    return maior, menor

def movimentacoes_mensais(movs):
    movs['AnoMes'] = pd.to_datetime(movs['DataMov']).dt.to_period('M')
    return movs.groupby(['AnoMes', 'TipoMov'])['Quantidade'].sum().unstack(fill_value=0)

def movimentacoes_por_usuario(movs, usuarios):
    movs_usuarios = movs.groupby('UsuarioID')['Quantidade'].sum().reset_index()
    return movs_usuarios.merge(usuarios, on='UsuarioID').sort_values(by='Quantidade', ascending=False)
