#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
# Hugo Enrique Florez Granados
#=======================================
# Definición de una excepción personalizada para errores relacionados con Cliente
class ClienteError(Exception):  # Se crea una clase que hereda de Exception (errores en Python)
    pass  # No se agrega lógica, solo sirve para identificar errores del cliente


# Definición de la clase Cliente
class Cliente:

    # Constructor de la clase (se ejecuta al crear un objeto)
    def __init__(self, nombre, edad, correo):
        self.set_nombre(nombre)  # Llama al método que valida y asigna el nombre
        self.set_edad(edad)      # Llama al método que valida y asigna la edad
        self.set_correo(correo)  # Llama al método que valida y asigna el correo

    
    # MÉTODOS SET (VALIDACIÓN)
    

    def set_nombre(self, nombre):
        # Verifica que el nombre sea texto y no esté vacío
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ClienteError("El nombre no puede estar vacío")  # Lanza un error si no cumple
        self.__nombre = nombre  # Guarda el nombre como atributo privado

    def set_edad(self, edad):
        # Verifica que la edad sea un número entero positivo
        if not isinstance(edad, int) or edad <= 0:
            raise ClienteError("La edad debe ser un número positivo")  # Lanza error
        self.__edad = edad  # Guarda la edad como atributo privado

    def set_correo(self, correo):
        # Verifica que el correo contenga el símbolo '@'
        if "@" not in correo:
            raise ClienteError("Correo inválido")  # Lanza error si no es válido
        self.__correo = correo  # Guarda el correo como atributo privado

   
    # MÉTODOS GET (OBTENER DATOS)
   

    def get_nombre(self):
        return self.__nombre  # Retorna el nombre almacenado

    def get_edad(self):
        return self.__edad  # Retorna la edad almacenada

    def get_correo(self):
        return self.__correo  # Retorna el correo almacenado

   
    # MÉTODO DE UTILIDAD
   

    def mostrar_info(self):
        # Retorna un texto con todos los datos del cliente
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"



# PROGRAMA PRINCIPAL (SIMULACIÓN)


# Verifica que este archivo se ejecute directamente
if __name__ == "__main__":

    print("=== PRUEBA DEL SISTEMA ===")  # Muestra título en consola

    
    # CASO 1: CLIENTE VÁLIDO
   
    try:
        # Se crea un cliente con datos correctos
        cliente1 = Cliente("Juan", 25, "juan@email.com")

        # Se imprime la información del cliente
        print(cliente1.mostrar_info())

    except ClienteError as e:
        # Este bloque no debería ejecutarse en este caso
        print("Error en cliente válido:", e)

    print("--------------------------")  # Separador visual

    
    # CASO 2: NOMBRE INVÁLIDO
    
    try:
        # Se intenta crear un cliente con nombre vacío
        cliente2 = Cliente("", 25, "correo@email.com")

    except ClienteError as e:
        # Captura el error generado por el nombre
        print("Error (nombre):", e)

        # Guarda el error en archivo de logs
        with open("logs.txt", "a") as archivo:
            archivo.write(f"Error nombre: {e}\n")

    print("--------------------------")

    
    # CASO 3: EDAD INVÁLIDA
    
    try:
        # Se intenta crear un cliente con edad negativa
        cliente3 = Cliente("Ana", -5, "ana@email.com")

    except ClienteError as e:
        # Captura el error de edad
        print("Error (edad):", e)

        # Guarda el error en logs
        with open("logs.txt", "a") as archivo:
            archivo.write(f"Error edad: {e}\n")

    print("--------------------------")

   
    # CASO 4: CORREO INVÁLIDO
    
    try:
        # Se intenta crear un cliente con correo incorrecto
        cliente4 = Cliente("Luis", 30, "correo_invalido")

    except ClienteError as e:
        # Captura el error de correo
        print("Error (correo):", e)

        # Guarda el error en logs
        with open("logs.txt", "a") as archivo:
            archivo.write(f"Error correo: {e}\n")