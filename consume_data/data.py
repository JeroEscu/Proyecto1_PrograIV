import os
import pandas as pd
import numpy as np
import consume_data.dataCleaning as dc
from unidecode import unidecode

def get_data(file_name):

    # Obtener la ruta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    # Construir la ruta relativa al archivo
    file_path = os.path.join(script_dir, file_name)
    # Cargar el archivo de Excel
    results_df = pd.read_excel(file_path, engine="openpyxl")

    return results_df

def normalize_data(df):

    # Renombrar columnas para que sean más cortas y sin tildes
    df = df.rename(columns={
        "pH agua:suelo 2,5:1,0": "pH",
        "Fósforo (P) Bray II mg/kg": "Fosforo",
        "Potasio (K) intercambiable cmol(+)/kg": "Potasio"
    })

    # Normalizar los valores de las columnas
    df["Departamento"] = df["Departamento"].apply(lambda x: unidecode(x).strip().upper())
    df["Municipio"] = df["Municipio"].apply(lambda x: unidecode(x).strip().upper())
    df["Cultivo"] = df["Cultivo"].apply(lambda x: unidecode(x).strip().upper())
    df["Topografia"] = df["Topografia"].apply(lambda x: unidecode(x).strip().upper())
    df = df.fillna("")

    return df
 
def filter_data(df, department, town, crop):

    df = normalize_data(df)

    filter_columns = (
        (df["Departamento"] == unidecode(department)) &
        (df["Municipio"] == unidecode(town)) &
        (df["Cultivo"] == unidecode(crop))
    )

    filter_df = df[filter_columns]
    filter_df = dc.clean_data(filter_df)

    return filter_df

def calculate_medians(df):

    median_values = df[["pH", "Fosforo", "Potasio"]].median()

    return median_values
