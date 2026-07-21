import os

import boto3

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

bucket = "projeto-residuo-bucket"
arquivo = "coletas_20260715.csv"

s3.download_file(
    bucket,
    arquivo,
    "coletas_20260715.csv"
)

print("Arquivo baixado com sucesso!")


