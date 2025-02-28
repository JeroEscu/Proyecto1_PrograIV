import consume_data.data as data
import ui.user as ui



def main():
    department, town, crop, num_registers = ui.user_input()
    df = data.get_data("resultado_laboratorio_suelo.xlsx")
    filtered_df = data.filter_data(df, department, town, crop, num_registers)
    #ui.display_data(filtered_df)
    #ui.display_verification(filtered_df, register)

   
main()