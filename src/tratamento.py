import os
import pandas as pd



CAMINHO_CSV = os.path.join(
    "/opt/airflow",
    "coletas_20260715.csv"
)

def ler_csv():
    print(">>novo tratamento<<")

    # Leitura do CSV
    df = pd.read_csv(
        CAMINHO_CSV,
        sep=";",
        encoding="cp1252"
    )

    print("CSV carregado com sucesso!\n")

    # Remove espaços em branco
    df = df.apply(
        lambda coluna: coluna.str.strip()
        if coluna.dtype == "object"
        else coluna
    )

    # Converte tipos
    df["data_coleta"] = pd.to_datetime(
        df["data_coleta"],
        dayfirst=True,
        errors="coerce"
    )

    df["peso_estimado"] = pd.to_numeric(
        df["peso_estimado"],
        errors="coerce"
    )

    # Coluna para registrar erros
    df["erro"] = ""

    # Nome da empresa vazio
    df.loc[
        (df["nome_empresa"].isna()) |
        (df["nome_empresa"] == ""),
        "erro"
    ] += "Nome da empresa vazio; "

    # CNPJ vazio
    df.loc[
        (df["cnpj"].isna()) |
        (df["cnpj"] == ""),
        "erro"
    ] += "CNPJ vazio; "

    # Tipo de resíduo vazio
    df.loc[
        (df["tipo_residuo"].isna()) |
        (df["tipo_residuo"] == ""),
        "erro"
    ] += "Tipo de resíduo vazio; "

    # Peso inválido
    df.loc[
        (df["peso_estimado"].isna()) |
        (df["peso_estimado"] <= 0),
        "erro"
    ] += "Peso inválido; "

    # Data inválida
    df.loc[
        df["data_coleta"].isna(),
        "erro"
    ] += "Data inválida; "

    # Separa registros válidos e inválidos
    validos = df[df["erro"] == ""].copy()
    invalidos = df[df["erro"] != ""].copy()

    print("=" * 50)
    print("RESUMO")
    print("=" * 50)

    print(f"Total de registros: {len(df)}")
    print(f"Registros válidos: {len(validos)}")
    print(f"Registros inválidos: {len(invalidos)}")

    print("\nRegistros inválidos:\n")
    print(invalidos)

    return validos, invalidos