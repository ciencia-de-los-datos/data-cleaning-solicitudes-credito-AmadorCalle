"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    data = "solicitudes_credito.csv"
    df = pd.read_csv(data, sep=";")
    df = df.drop(columns=['Unnamed: 0'])
    df = df.dropna().drop_duplicates()
    df['sexo'] = df['sexo'].str.upper()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.upper()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper()
    df['barrio'] = df['barrio'].str.lower().str.replace('_', '-').str.replace('-',' ')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '', regex = False).str.replace(',', '').str.replace(' ', '').astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst = True)
    df = df.drop_duplicates().dropna()
    return df
