#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
class ClienteError(Exception):  # Se define una excepción personalizada para errores del cliente
    pass  # No se agrega lógica adicional, solo identifica el tipo de error


class Cliente:  # Se define la clase Cliente

    def __init__(self, nombre, edad, correo):  # Constructor que se ejecuta al crear un objeto
        self.set_nombre(nombre)  # Llama al método que valida y asigna el nombre
        self.set_edad(edad)  # Llama al método que valida y asigna la edad
        self.set_correo(correo)  # Llama al método que valida y asigna el correo

    def set_nombre(self, nombre):  # Método para establecer el nombre
        if not isinstance(nombre, str) or nombre.strip() == "":  # Verifica que sea texto y no esté vacío
            raise ClienteError("El nombre no puede estar vacío")  # Lanza un error si no cumple la condición
        self.__nombre = nombre  # Guarda el nombre como atributo privado

    def set_edad(self, edad):  # Método para establecer la edad
        if not isinstance(edad, int) or edad <= 0:  # Verifica que sea entero y positivo
            raise ClienteError("La edad debe ser un número positivo")  # Lanza error si no cumple
        self.__edad = edad  # Guarda la edad como atributo privado

    def set_correo(self, correo):  # Método para establecer el correo
        if "@" not in correo:  # Verifica que el correo contenga '@'
            raise ClienteError("Correo inválido")  # Lanza error si el correo no es válido
        self.__correo = correo  # Guarda el correo como atributo privado

    def get_nombre(self):  # Método para obtener el nombre
        return self.__nombre  # Retorna el valor del nombre

    def get_edad(self):  # Método para obtener la edad
        return self.__edad  # Retorna el valor de la edad

    def get_correo(self):  # Método para obtener el correo
        return self.__correo  # Retorna el valor del correo

    def mostrar_info(self):  # Método para mostrar la información del cliente
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"  # Retorna un texto con los datos


if __name__ "__main__":  # Verifica que el archivo se ejecute directamente

    print("=== PRUEBA DEL SISTEMA ===")  # Imprime un mensaje de inicio

    try:  # Inicia un bloque para manejar posibles errores
        cliente1 = Cliente("Juan", 25, "juan@email.com")  # Crea un cliente válido
        print(cliente1.mostrar_info())  # Muestra la información del cliente

        cliente2 = Cliente("", -5, "correo_invalido")  # Intenta crear un cliente inválido

    except ClienteError as e:  # Captura errores del tipo ClienteError
        print("Se capturó un error:", e)  # Muestra el error en consola

        with open("logs.txt", "a") as archivo:  # Abre (o crea) el archivo logs.txt en modo agregar
            archivo.write(f"Error en Cliente: {e}\n")  # Escribe el error en el archivo
