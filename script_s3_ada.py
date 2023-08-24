from datetime import datetime
import os
import boto3

BUCKET_NAME = "projeto-final-ada"


def send_files():
    # variáveis AWS
    client = boto3.client('s3')

    # Paths
    path = os.getcwd()
    arquivos = os.listdir('files')

    if len(arquivos) <= 0:
        print('Não existem relatórios pendentes para integração!')
    else:
        for arq in arquivos:
            filename = os.path.join(path, 'files', arq)
            with open(filename, 'rb') as data:
                # Envia itens para o S3
                client.upload_file(filename, BUCKET_NAME, arq)

            # Guarda a data e hora da integração
            now = str(datetime.now()).replace(':', '').replace('.', '').replace(' ', '')

            # Move o arquivo da pasta files para logs
            os.rename(filename, os.path.join(path, 'log_integracao', f'{now}_{arq}'))
            print(f'Arquivo {arq} integrado e movido para a pasta de logs!')

        client.close()
        print('Itens integrados com sucesso!')


if __name__ == '__main__':
    send_files()
