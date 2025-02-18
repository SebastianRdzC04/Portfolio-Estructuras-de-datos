VALUES = {
    "A": 10, "B": 20, "C": 30, "D": 40, "E": 50, "F": 60, "G": 70,
    "H": 80, "I": 90, "J": 100, "K": 110, "L": 120, "M": 130, "N": 140,
    "O": 150, "P": 160, "Q": 170, "R": 180, "S": 190, "T": 200, "U": 210,
    "V": 220, "W": 230, "X": 240, "Y": 250, "Z": 260, "a": 15, "b": 25,
    "c": 35, "d": 45, "e": 55, "f": 65, "g": 75, "h": 85, "i": 95,
    "j": 105, "k": 115, "l": 125, "m": 135, "n": 145, "o": 155, "p": 165,
    "q": 175, "r": 185, "s": 195, "t": 205, "u": 215, "v": 225, "w": 235,
    "x": 245, "y": 255, "z": 265
}

class ARRAY:
    def __init__(self, n):
        self.array: list = [0] * n 
        self.n: int = 0 
    
    def show_array(self):
        if self.n == 0:
            print("No hay elementos en el array")
            return
        print("Array:", self.array[:self.n])
    
    def search_array(self, value: chr):
        if self.n == 0:
            print("No hay elementos en el array")
            return -1
        for i in range(self.n):
            if self.array[i] == value:
                return i
        return -1
    
    def insert_value(self, value: chr):
        if self.n == len(self.array):
            print("No hay espacio en el array")
            return
        converted_value = VALUES[value]
        if self.n == 0: 
            self.array[0] = value
            self.n = 1 
            return self.array

        location_to_insert = self.n
        for i in range(self.n): 
            if VALUES[self.array[i]] > converted_value:
                location_to_insert = i
                break

        for i in range(self.n, location_to_insert, -1):
            self.array[i] = self.array[i - 1]
        
        # Inserta el valor en el lugar correcto
        self.array[location_to_insert] = value
        self.n += 1 
        return self.array
    
    def delete_value(self, value: chr):
        if self.n == 0:  # Si el array está vacío
            print("No hay elementos en el array")
            return
        location_to_delete = self.search_array(value)
        if location_to_delete == -1:
            print("No se ha encontrado el valor")
            return
        

        for i in range(location_to_delete, self.n - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.n - 1] = 0 
        self.n -= 1
        return self.array

if __name__ == "__main__":
    user_array = ARRAY(20)

    user_input = input("Selecciona una opción: \n"
                       "1.- Mostrar array\n"
                       "2.- Buscar valor\n"
                       "3.- Insertar valor\n"
                       "4.- Eliminar valor\n")

    while user_input != "exit":
        if user_input == "1":
            user_array.show_array()
        elif user_input == "2":
            value = input("Introduce el valor a buscar: ")
            print("Índice:", user_array.search_array(value))
        elif user_input == "3":
            value = input("Introduce el valor a insertar: ")
            user_array.insert_value(value)
        elif user_input == "4":
            value = input("Introduce el valor a eliminar: ")
            user_array.delete_value(value)

        user_input = input("Selecciona una opción: \n"
                           "1.- Mostrar array\n"
                           "2.- Buscar valor\n"
                           "3.- Insertar valor\n"
                           "4.- Eliminar valor\n")

    print("Saliendo del programa...")
    print("Array final:", user_array.array)
