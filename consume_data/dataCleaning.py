import pandas as pd
import numpy as np
import re

def correct_ph(df):

    # Convertir los valores de la columna "pH" a float
    df.loc[:,"pH"] = pd.to_numeric(df["pH"], errors="coerce")
    # Calcular la mediana de los valores válidos (<=1000)
    ph_median = df.loc[df["pH"] <= 1000, "pH"].median()
    # Reemplazar valores mayores a 1000 con la mediana
    df.loc[df["pH"] > 1000, "pH"] = ph_median

    return df

def correct_phosphorus(value):
    try:
        value_str = str(int(value))  # Convertir a string eliminando decimales innecesarios
        
        if len(value_str) == 17:  
            return float(value_str[:2] + "." + value_str[2:])  # 2 enteros, el resto decimal
        elif len(value_str) == 16:  
            return float(value_str[:1] + "." + value_str[1:])  # 1 entero, el resto decimal
        elif len(value_str) == 15:  
            return float("0." + value_str)
        else:  
            return np.nan  # Valores inválidos se convierten en NaN
    except:
        return np.nan  # Manejar cualquier error con NaN

def correct_potassium(value):
    
    if (value < 0):
        return float(value * -1)
    elif(value > 0) and (value < 1):
        return float(value)
    else:
        value_str = str(int(value))  # Convertir a string eliminando decimales innecesarios
        if len(value_str) > 5:  
            return float("0." + value_str) # 0 entero, el resto decimal
        else:  
            return np.nan  # Valores inválidos se convierten en NaN
            

def clean_data(df):

    df = correct_ph(df)

    # Convertir los valores de la columna "Fosforo" a float
    df.loc[:,"Fosforo"] = pd.to_numeric(df["Fosforo"], errors="coerce")
    # Aplicar la función correct_phosphorus a la columna "Fosforo"
    df.loc[:,"Fosforo"] = df["Fosforo"].apply(correct_phosphorus)
    # Reemplazar los valores NaN con la mediana de los valores válidos
    phosphorus_median = df["Fosforo"].median()
    df.loc[:,"Fosforo"].fillna(phosphorus_median, inplace=True)

    # Convertir los valores de la columna "Potasio" a float
    df.loc[:,"Potasio"] = pd.to_numeric(df["Potasio"], errors="coerce")
    # Aplicar la función correct_potassium a la columna "Potasio"
    df.loc[:,"Potasio"] = df["Potasio"].apply(correct_potassium)
    # Reemplazar los valores NaN con la mediana de los valores válidos
    potassium_median = df["Potasio"].median()
    df.loc[:,"Potasio"].fillna(potassium_median, inplace=True)

    return df
