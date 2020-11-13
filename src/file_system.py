from urllib.request import urlretrieve
from zipfile import ZipFile
import pandas as  pd
import os
import codecs
from model_db import create_connection

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(ROOT_DIR, 'files/DGII_RNC.zip')
rnc_file_path = os.path.join(ROOT_DIR, 'files/TMP/DGII_RNC.TXT')


def download_file():
    print("downloading file...")
    url = "https://dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"
    urlretrieve(url, zip_path)


def unzip_file():
    print("unzping file...")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(ROOT_DIR + '/files')

def importDataToDb():
    print("reading file...")
    df = pd.read_csv(rnc_file_path, sep='|', encoding='ISO-8859-1', header=None)
    cols = [4,5,6,7]
    df.drop(df.columns[cols], axis=1, inplace=True)
    df.columns = ['rnc_cedula', 'business_name', 'comercial_name', 'service_type', 'registered_date', 'state', 'payment_scheme']

    conn = create_connection()
    print("importing file to db...")
    df.to_sql('taxpayers', conn, if_exists='replace', index=False)


def execute():
    download_file()
    unzip_file()
    importDataToDb()


if __name__ == "__main__":
    execute()
