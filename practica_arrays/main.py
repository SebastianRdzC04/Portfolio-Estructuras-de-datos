
VALUES = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40,
    "E": 50,
    "F": 60,
    "G": 70,
    "H": 80,
    "I": 90,
    "J": 100,
    "K": 110,
    "L": 120,
    "M": 130,
    "N": 140,
    "O": 150,
    "P": 160,
    "Q": 170,
    "R": 180,
    "S": 190,
    "T": 200,
    "U": 210,
    "V": 220,
    "W": 230,
    "X": 240,
    "Y": 250,
    "Z": 260,
    "a": 15,
    "b": 25,
    "c": 35,
    "d": 45,
    "e": 55,
    "f": 65,
    "g": 75,
    "h": 85,
    "i": 95,
    "j": 105,
    "k": 115,
    "l": 125,
    "m": 135,
    "n": 145,
    "o": 155,
    "p": 165,
    "q": 175,
    "r": 185,
    "s": 195,
    "t": 205,
    "u": 215,
    "v": 225,
    "w": 235,
    "x": 245,
    "y": 255,
    "z": 265
}



def inicializate_array(n):
    """
    Inicializa un array de n elementos con el valor 0
    :param n: int
    :return: list
    """
    return [0] * n, -1

def show_array(sended_array, n):
    if n == -1:
        print("No hay elementos en el array")
        return
    for i in range(n):
        print(sended_array[i])

def search_array(sended_array, n, value):
    for i in range(n):
        if sended_array[i] == value:
            return i
    return -1

def insert_value(sended_array, n, value):
    converted_value = VALUES[value]
    location_to_insert = 0
    for i in range(n):
        if VALUES[sended_array[i]] > value:
            location_to_insert = i
            break
    for i in range(n, location_to_insert, -1):
        if i == location_to_insert:
            sended_array[i] = value
        else:
            sended_array[i] = sended_array[i - 1]
    return sended_array

def delete_value(sended_array, n, value):
    location_to_delete = search_array(sended_array, n, value)
    if location_to_delete == -1:
        print("No se ha encontrado el valor")
        return
    for i in range(location_to_delete, n):
        sended_array[i] = sended_array[i + 1]
    n -= 1
    return sended_array, n
    


if __name__ == "__main__":
    user_array, n = inicializate_array(20)
    user_input = input("Selecciona una opcion: \n"
                       "1. Mostrar el array \n"
                       "2. Buscar un valor en el array \n"
                       "3. Insertar un valor en el array \n"
                       "4. Eliminar un valor del array \n")
    while user_input != "exit":
        if user_input == "1":
            show_array(user_array, n)
        elif user_input == "2":
            value_to_search = input("Introduce el valor a buscar: ")
            print(search_array(user_array, n, value_to_search))
        elif user_input == "3":
            value_to_insert = input("Introduce el valor a insertar: ")
            user_array = insert_value(user_array, n, value_to_insert)
            n += 1
        elif user_input == "4":
            value_to_delete = input("Introduce el valor a eliminar: ")
            user_array, n = delete_value(user_array, n, value_to_delete)
        user_input = input("Selecciona una opcion: \n"
                       "1. Mostrar el array \n"
                       "2. Buscar un valor en el array \n"
                       "3. Insertar un valor en el array \n"
                       "4. Eliminar un valor del array \n")
