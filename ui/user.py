def user_input():
    department = input("Ingrese el nombre del departamento que desea consultar: ").upper()
    town = input("Ingrese el nombre del municipio que desea consultar: ").upper()
    crop = input("Ingrese el nombre del cultivo que desea consultar: ").upper()
    num_registers = int(input("Ingrese el número de registros que desea consultar: "))

    return department, town, crop, num_registers