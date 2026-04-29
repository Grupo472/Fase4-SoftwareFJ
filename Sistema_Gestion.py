#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
# Hugo Enrique Florez Granados
#==============================================================================
# Se importan las librerías necesarias para el funcionamiento del sistema, incluyendo

import re #re para expresiones regulares, utilizado para validar formatos de correo electrónico y otros datos de entrada.
import uuid # uuid para generación de identificadores únicos.
import logging # logging para registro de eventos.
import os #os para operaciones del sistema operativo.
from abc import ABC, abstractmethod # abc para clases abstractas
from datetime import datetime #  datetime para manejo de fechas y horas.
#===============================================================================
# CONFIGURACIÓN DEL LOGGER
# Registra errores y eventos en un archivo .log
#==|=============================================================================
os.makedirs("logs", exist_ok=True) # Crea el directorio logs si no existe
logging.basicConfig( # Configuración del logger para registrar eventos en un archivo de logs
    filename="logs/sistema.log", # Archivo donde se guardarán los logs
    level=logging.INFO, # Nivel de log para registrar solo eventos de información y errores
    format="%(asctime)s - %(levelname)s - %(message)s", # Formato del mensaje de log que incluye la fecha, el nivel de log y el mensaje
    encoding="utf-8" # Codificación del archivo de log para soportar caracteres especiales
)
logger = logging.getLogger(__name__) # Obtiene un logger específico para este módulo, lo que permite registrar eventos relacionados con el sistema de gestión de clientes, servicios y reservas.
#=|=============================================================================
#===============================================================================
# EXCEPCIONES PERSONALIZADAS
# ================================================================================
class ErrorSistema(Exception):
    # Excepción base del sistema
    def __init__(self, mensaje):
        super().__init__(mensaje)
        logger.error(f"[ERROR] {mensaje}")

class ClienteError(ErrorSistema):
    # Error en datos del cliente
    def __init__(self, mensaje):
        super().__init__(f"ClienteError: {mensaje}")

class ServicioError(ErrorSistema):
    # Error en un servicio
    def __init__(self, mensaje):
        super().__init__(f"ServicioError: {mensaje}")

class ReservaError(ErrorSistema):
    # Error en una reserva
    def __init__(self, mensaje):
        super().__init__(f"ReservaError: {mensaje}")
#==============================================================================
# DEFINICION ENTIDAD BASE
#==============================================================================
class EntidadSistema(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Define la interfaz común: describir y validar.
    """

    @abstractmethod
    def describir(self) -> str:
        """Retorna una descripción textual de la entidad."""
        pass

    @abstractmethod
    def validar(self) -> bool:
        """Valida que la entidad esté en un estado correcto."""
        pass
#==============================================================================
class Cliente:  # Definición de la clase Cliente

    def __init__(self, nombre, edad, correo):  # Constructor que inicializa los atributos del cliente
        try:  # Se intenta ejecutar el bloque de código que puede generar errores
            self.set_nombre(nombre)  # Se llama al método para validar y asignar el nombre
            self.set_edad(edad)  # Se llama al método para validar y asignar la edad
            self.set_correo(correo)  # Se llama al método para validar y asignar el correo
        except Exception as e:  # Captura cualquier excepción que ocurra
            self.registrar_error(e)  # Se registra el error en un archivo de logs
            raise  # Se vuelve a lanzar la excepción para que no se oculte el error

    #  Encapsulación con setters y getters

    def set_nombre(self, nombre):  # Método para establecer el nombre del cliente
        if not isinstance(nombre, str) or nombre.strip() == "":  # Verifica que el nombre sea texto y no esté vacío
            raise ValueError("El nombre no puede estar vacío")  # Lanza un error si la validación falla
        self.__nombre = nombre  # Guarda el nombre como atributo privado

    def get_nombre(self):  # Método para obtener el nombre del cliente
        return self.__nombre  # Retorna el valor del nombre

    def set_edad(self, edad):  # Método para establecer la edad del cliente
        if not isinstance(edad, int) or edad <= 0:  # Verifica que la edad sea un número entero positivo
            raise ValueError("La edad debe ser un número positivo")  # Lanza un error si la validación falla
        self.__edad = edad  # Guarda la edad como atributo privado

    def get_edad(self):  # Método para obtener la edad del cliente
        return self.__edad  # Retorna el valor de la edad

    def set_correo(self, correo):  # Método para establecer el correo del cliente
        if "@" not in correo:  # Verifica que el correo tenga el símbolo @
            raise ValueError("Correo inválido")  # Lanza un error si no es válido
        self.__correo = correo  # Guarda el correo como atributo privado

    def get_correo(self):  # Método para obtener el correo del cliente
        return self.__correo  # Retorna el valor del correo

    #  Método para mostrar información del cliente
    def mostrar_info(self):  # Método que devuelve los datos del cliente en texto
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"  # Retorna un string con los datos

    #  Método para registrar errores en archivo
    def registrar_error(self, error):  # Método que recibe un error
        with open("logs.txt", "a") as archivo:  # Abre (o crea) el archivo logs.txt en modo agregar
            archivo.write(f"Error en Cliente: {error}\n")  # Escribe el error en el archivo


if __name__ == "__main__":  # Punto de entrada del programa
    
    print("=== PRUEBA DEL SISTEMA ===")  # Mensaje de inicio

    try:
        cliente1 = Cliente("Juan", 25, "juan@email.com")
        print(cliente1.mostrar_info())

        cliente2 = Cliente("", -5, "correo_invalido")  # Genera error

    except Exception as e:
        print("Se capturó un error:", e) 


