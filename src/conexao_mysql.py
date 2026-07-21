import os
import mysql.connector


def conectar():

    print(">> CONEXÃO MYSQL <<")

    conexao = mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")
    )

    return conexao


def buscar_cliente(cursor, cnpj):

    sql = """
    SELECT id_cliente
    FROM tb_cliente
    WHERE cnpj = %s
    """

    cursor.execute(sql, (cnpj,))
    return cursor.fetchone()


def buscar_tipo_residuo(cursor, nome):

    sql = """
    SELECT id_tipo_residuo
    FROM tb_tipo_residuo
    WHERE nome = %s
    """

    cursor.execute(sql, (nome,))
    return cursor.fetchone()


def inserir_solicitacao(cursor, id_cliente, id_tipo, peso):

    sql = """
    INSERT INTO tb_solicitacao_coleta
    (
        data_solicitacao,
        peso_estimado,
        status,
        observacao,
        data_importacao,
        tb_cliente_id_cliente,
        tb_tipo_residuo_id_tipo_residuo
    )
    VALUES
    (
        NOW(),
        %s,
        'PENDENTE',
        'Importado via ETL',
        NOW(),
        %s,
        %s
    )
    """

    cursor.execute(
        sql,
        (
            peso,
            id_cliente,
            id_tipo
        )
    )


def inserir_log(
    cursor,
    arquivo,
    inicio,
    fim,
    lidos,
    importados,
    invalidos,
    status
):

    sql = """
    INSERT INTO tb_log_processamento
    (
        nome_arquivo,
        data_hora_inicio,
        data_hora_fim,
        registros_lidos,
        registros_importados,
        registros_invalidos,
        status_execucao
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            arquivo,
            inicio,
            fim,
            lidos,
            importados,
            invalidos,
            status
        )
    )