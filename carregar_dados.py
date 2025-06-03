import pandas as pd

def carregar_tabelas(conn):
    produtos = pd.read_sql('SELECT * FROM Produtos', conn)
    movs = pd.read_sql('SELECT * FROM Movimentacoes', conn)
    usuarios = pd.read_sql('SELECT * FROM Usuarios', conn)
    compras = pd.read_sql('SELECT * FROM Compras', conn)
    fornecedores = pd.read_sql('SELECT * FROM Fornecedores', conn)
    categorias = pd.read_sql('SELECT * FROM Categorias', conn)
    return produtos, movs, usuarios, compras, fornecedores, categorias
