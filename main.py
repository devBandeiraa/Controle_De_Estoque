import os
import pandas as pd
from tabulate import tabulate
from conexao import conectar
from carregar_dados import carregar_tabelas
from analises import (
    movimentacoes_por_produto,
    valor_estoque_por_categoria,
    produtos_extremos,
    movimentacoes_mensais,
    movimentacoes_por_usuario
)
from visualizacoes import (
    plot_valor_categoria,
    plot_fornecedores
)

# Conectar e carregar
conn = conectar()
produtos, movs, usuarios, compras, fornecedores, categorias = carregar_tabelas(conn)

# Criar pasta de relatórios se não existir
os.makedirs("relatorios", exist_ok=True)

# 1. Movimentações por produto
mov_prod = movimentacoes_por_produto(movs, produtos)
mov_prod.to_csv("relatorios/movimentacoes_por_produto.csv", index=False)
print("\n🔹 Movimentações por produto:")
print(tabulate(mov_prod, headers="keys", tablefmt="grid", showindex=False))

# 2. Valor em estoque por categoria
valor_cat = valor_estoque_por_categoria(produtos, categorias)
print("\n🔹 Valor do estoque por categoria:")
print(tabulate(valor_cat, headers="keys", tablefmt="fancy_grid", showindex=False))

# 3. Produtos com maior e menor valor em estoque
maior, menor = produtos_extremos(produtos)
pd.DataFrame([maior]).to_csv("relatorios/produto_maior_valor.csv", index=False)
pd.DataFrame([menor]).to_csv("relatorios/produto_menor_valor.csv", index=False)

print("\n🔹 Produto com maior valor em estoque:")
print(tabulate(pd.DataFrame([maior]), headers="keys", tablefmt="github", showindex=False))

print("\n🔹 Produto com menor valor em estoque:")
print(tabulate(pd.DataFrame([menor]), headers="keys", tablefmt="github", showindex=False))

# 4. Movimentações mensais
mov_mensal = movimentacoes_mensais(movs)
mov_mensal.to_csv("relatorios/movimentacoes_mensais.csv")
print("\n🔹 Movimentações mensais:")
print(tabulate(mov_mensal, headers="keys", tablefmt="grid", showindex=False))

# 5. Movimentações por usuário
mov_usuarios = movimentacoes_por_usuario(movs, usuarios)
mov_usuarios.to_csv("relatorios/movimentacoes_por_usuario.csv", index=False)
print("\n🔹 Movimentações por usuário:")
print(tabulate(mov_usuarios[['Nome', 'Cargo', 'Quantidade']], headers="keys", tablefmt="grid", showindex=False))

# Visualizações
plot_valor_categoria(valor_cat)
plot_fornecedores(compras, fornecedores)
