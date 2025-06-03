from conexao import conectar
from carregar_dados import carregar_tabelas
from analises import *
from visualizacoes import *


# Conectar e carregar
conn = conectar()
produtos, movs, usuarios, compras, fornecedores, categorias = carregar_tabelas(conn)

from analises import (
    movimentacoes_por_produto,
    valor_estoque_por_categoria,
    produtos_extremos,
    movimentacoes_mensais,
    movimentacoes_por_usuario
)
import os

# Criar pasta de relatórios se não existir
os.makedirs("relatorios", exist_ok=True)

# 1. Movimentações por produto
mov_prod = movimentacoes_por_produto(movs, produtos)
mov_prod.to_csv("relatorios/movimentacoes_por_produto.csv", index=False)

# 2. Valor em estoque por categoria
valor_cat = valor_estoque_por_categoria(produtos, categorias)
valor_cat.to_csv("relatorios/valor_estoque_por_categoria.csv")

# 3. Produtos com maior e menor valor em estoque
maior, menor = produtos_extremos(produtos)
pd.DataFrame([maior]).to_csv("relatorios/produto_maior_valor.csv", index=False)
pd.DataFrame([menor]).to_csv("relatorios/produto_menor_valor.csv", index=False)

# 4. Movimentações mensais
mov_mensal = movimentacoes_mensais(movs)
mov_mensal.to_csv("relatorios/movimentacoes_mensais.csv")

# 5. Movimentações por usuário
mov_usuarios = movimentacoes_por_usuario(movs, usuarios)
mov_usuarios.to_csv("relatorios/movimentacoes_por_usuario.csv", index=False)


# Executar análises
print(movimentacoes_por_produto(movs, produtos))
print(valor_estoque_por_categoria(produtos, categorias))

maior, menor = produtos_extremos(produtos)
print("Produto com maior valor em estoque:", maior['Nome'], "-", maior['ValorTotalEstoque'])
print("Produto com menor valor em estoque:", menor['Nome'], "-", menor['ValorTotalEstoque'])

print(movimentacoes_mensais(movs))
print(movimentacoes_por_usuario(movs, usuarios)[['Nome', 'Cargo', 'Quantidade']])

# Visualizações
plot_valor_categoria(valor_estoque_por_categoria(produtos, categorias))
plot_fornecedores(compras, fornecedores)


