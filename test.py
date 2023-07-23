import sw_functions as sw

def get_data():


    with open ("database.csv","r") as file:
        lineas = file.readlines()
        id_counter = 1

        for linea in lineas:
            username,password = linea.split(",")

            id_counter = id_counter + 1


