from datetime import datetime
import os
import boto3


def send_files():
    # variáveis AWS
    client = boto3.client('s3')
    bucket = 'projeto-final-ada'

    # Paths
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
            now = str(datetime.now()).replace(':', '').replace('.', '').replace(' ', '')
            os.rename(os.path.join(cur_path, arq), os.path.join(logs_path, f'{now}_{arq}'))
            print(f'Arquivo {arq} integrado e movido para a pasta de logs!')

        client.close()

        print('Itens integrados com sucesso!')


if __name__ == '__main__':
    send_files()
