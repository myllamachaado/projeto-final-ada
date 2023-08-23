from datetime import datetime
import os
import boto3


client = boto3.client('s3')
bucket = 'projeto-final-ada'
cur_path = os.path.join(os.getcwd(), 'files')
logs_path = os.path.join(os.getcwd(), 'log_integracao')
arquivos = os.listdir('files')

if len(arquivos) <= 0:
    print('Não existem relatórios pendentes para integração!')
else:
    for arq in arquivos:
        filename = os.path.join(cur_path, arq)
        data = open(filename, 'rb')
        # Envia itens para o S3
        client.upload_file(filename, bucket, arq)
        data.close()

    client.close()

    for arq in arquivos:
        # Move os arquivos para a pasta de logs
        now = str(datetime.now()).replace(':', '').replace('.', '').replace(' ', '')
        os.rename(os.path.join(cur_path, arq), os.path.join(logs_path, f'{now}_{arq}'))

    print('Itens integrados com sucesso!')
