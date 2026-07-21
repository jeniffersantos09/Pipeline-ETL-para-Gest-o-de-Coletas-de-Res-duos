from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sys

sys.path.append("/opt/airflow/src")

from tratamento import ler_csv
from conexao_mysql import (
    conectar,
    buscar_cliente,
    buscar_tipo_residuo,
    inserir_solicitacao,
    inserir_log
)


def executar_pipeline():

    inicio = datetime.now()

    validos, invalidos = ler_csv()

    conexao = conectar()

    cursor = conexao.cursor()

    importados = 0

    for _, linha in validos.iterrows():

        cliente = buscar_cliente(
            cursor,
            linha["cnpj"]
        )

        tipo = buscar_tipo_residuo(
            cursor,
            linha["tipo_residuo"]
        )

        if cliente and tipo:

            inserir_solicitacao(
                cursor,
                cliente[0],
                tipo[0],
                linha["peso_estimado"]
            )

            importados += 1

    inserir_log(
        cursor,
        "coletas_20260715.csv",
        inicio,
        datetime.now(),
        len(validos) + len(invalidos),
        importados,
        len(invalidos),
        "SUCESSO"
    )

    conexao.commit()

    cursor.close()

    conexao.close()

    print("=" * 50)
    print("PIPELINE EXECUTADO COM SUCESSO")
    print("=" * 50)
    print(f"Importados: {importados}")
    print(f"Inválidos: {len(invalidos)}")


with DAG(

    dag_id="pipeline_residuos",

    start_date=datetime(2026, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=["etl", "python", "mysql"],

) as dag:

    executar = PythonOperator(

        task_id="executar_pipeline",

        python_callable=executar_pipeline

    )