"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from unidecode import unidecode


def clean_data():
    data = "solicitudes_credito.csv"
    df = pd.read_csv(data, sep=";")
    df = df.drop(columns=['Unnamed: 0'])
    df['sexo'] = df['sexo'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper().apply(lambda fila: unidecode(fila))
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper().apply(lambda fila: unidecode(fila))
    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ').str.replace('-',' ').str.strip().str.upper().apply(lambda fila: unidecode(fila))
    df['monto_del_credito'] = df['monto_del_credito']=df['monto_del_credito'].apply(lambda fila: int(round(float(fila[2:].replace(',','')),0)) if fila.isnumeric() == False else int(fila))
    
    lista = df['fecha_de_beneficio'].apply(lambda fila: fila.split('/'))
    lista_temp = []
    for i in lista:
        if len(i[0]) == 4:
           lista_temp.append('/'.join([i[-1],i[1],i[0]]))
        else:
           lista_temp.append('/'.join(i))
    df['fecha_de_beneficio'] = lista_temp
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format = "%d/%m/%Y")    
    df = df.drop_duplicates().dropna()
    return df
