import os
import pandas as pd

def get_data(file_name):

    # Obtener la ruta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    # Construir la ruta relativa al archivo
    file_path = os.path.join(script_dir, file_name)
    # Cargar el archivo de Excel
    results_df = pd.read_excel(file_path, engine="openpyxl")

    return results_df
 
def filter_data(df, department, town, crop, num_registers):

    filter_columns = (
        (df["Departamento"] == department) &
        (df["Municipio"] == town) &
        (df["Cultivo"] == crop)
    )

    filter_df = df[filter_columns]

    # Mostrar los datos filtrados
    print("\nRegistros encontrados:")
    print(filter_df.head(num_registers)) #TODO: Cambiar la forma en que se indica el límite de registros

    return filter_df

