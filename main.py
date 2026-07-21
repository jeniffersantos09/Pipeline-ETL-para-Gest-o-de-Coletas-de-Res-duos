from datetime import datetime

from src.tratamento import ler_csv
from src.conexao_mysql import (
    conectar,
    buscar_cliente,
    buscar_tipo_residuo,
    inserir_solicitacao,
    inserir_log
)

# Horário de início
inicio = datetime.now()

# Lê e trata o CSV
validos, invalidos = ler_csv()

# Conecta ao banco
conexao = conectar()
cursor = conexao.cursor()

registros_importados = 0

# Percorre somente os registros válidos
for _, linha in validos.iterrows():

    cliente = buscar_cliente(cursor, linha["cnpj"])
    tipo = buscar_tipo_residuo(cursor, linha["tipo_residuo"])

    # Só importa se cliente e tipo existirem
    if cliente and tipo:

        inserir_solicitacao(
            cursor,
            cliente[0],
            tipo[0],
            linha["peso_estimado"]
        )

        registros_importados += 1

# Horário de término
fim = datetime.now()

# Grava o log
inserir_log(
    cursor,
    "coletas_20260715.csv",
    inicio,
    fim,
    len(validos) + len(invalidos),
    registros_importados,
    len(invalidos),
    "SUCESSO"
)

# Salva alterações
conexao.commit()

# Fecha conexão
cursor.close()
conexao.close()

print("\n==============================")
print("PROCESSAMENTO FINALIZADO")
print("==============================")
print(f"Registros lidos: {len(validos) + len(invalidos)}")
print(f"Importados: {registros_importados}")
print(f"Inválidos: {len(invalidos)}")