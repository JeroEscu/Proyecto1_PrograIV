def user_input():
    department = input("Ingrese el nombre del departamento que desea consultar: ").strip().upper()
    town = input("Ingrese el nombre del municipio que desea consultar: ").strip().upper()
    crop = input("Ingrese el nombre del cultivo que desea consultar: ").strip().upper()
    num_registers = int(input("Ingrese el número de registros que desea consultar: "))

    return department, town, crop, num_registers

def display_data(df, num_registers, median_values):

    if df.empty:
        print("\nNo se encontraron datos para el departamento, municipio o cultivo ingresados.")
    else:
        df = df.head(num_registers)
        columns_to_select = ["Departamento", "Municipio", "Cultivo", "Topografia", "pH", "Fosforo", "Potasio"]
        select_df = df[columns_to_select]
        print(select_df)
        print("\nMediana de los valores de pH, Fósforo y Potasio:")
        print(median_values)