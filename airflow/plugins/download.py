import logging
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from settings import BASE_URL, FILE_TABLES

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)


def download_and_unzip(base_url: str, file: str) -> None:
    '''
    Função para fazer download e descompactar os arquivos da Ancine

    args:
        - base_url: url base para download
        - file: arquivo que completa a url para download
    '''
    try:
        url = base_url + file
        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))

        msg = f'{file} - Arquivo Zip lido com Sucesso!'
        log.info(msg)

        # prefix_file = file.split('-csv')[0]
        extract_to = f'./downloads/{file}'
        zipfile.extractall(path=extract_to)

        msg = f'{file} - Descompactamento e Download feitos com Sucesso!'
        log.info(msg)
    except Exception as e:
        msg = f'{file} - {e}'
        log.error(msg)


if __name__ == '__main__':
    for file in FILE_TABLES:
        download_and_unzip(BASE_URL, file)
