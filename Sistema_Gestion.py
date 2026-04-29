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
os.makedirs("logs", exist_ok=True) # Crea el directorio logs si no existe
logging.basicConfig( # Configuración del logger para registrar eventos en un archivo de logs
    filename="logs/sistema.log", # Archivo donde se guardarán los logs
    level=logging.INFO, # Nivel de log para registrar solo eventos de información y errores
    format="%(asctime)s - %(levelname)s - %(message)s", # Formato del mensaje de log que incluye la fecha, el nivel de log y el mensaje
    encoding="utf-8" # Codificación del archivo de log para soportar caracteres especiales
)
logger = logging.getLogger(__name__) # Obtiene un logger específico para este módulo, lo que permite registrar eventos relacionados con el sistema de gestión de clientes, servicios y reservas.
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
# CLASE CLIENTE  # Tu rama integracion corregida
#=======================================

class Cliente:  # Define la clase Cliente

    def __init__(self, nombre, edad, correo):  # Constructor
        self.set_nombre(nombre)  # Llama método para validar y asignar nombre
        self.set_edad(edad)  # Llama método para validar y asignar edad
        self.set_correo(correo)  # Llama método para validar y asignar correo

    def set_nombre(self, nombre):  # Método para establecer nombre
        if not isinstance(nombre, str) or nombre.strip() == "":  # Valida tipo y vacío
            raise ClienteError("El nombre no puede estar vacío")  # Lanza excepción personalizada
        self.__nombre = nombre  # Guarda el nombre como atributo privado

    def set_edad(self, edad):  # Método para establecer edad
        if not isinstance(edad, int) or edad <= 0:  # Valida entero positivo
            raise ClienteError("La edad debe ser un número positivo")  # Lanza error
        self.__edad = edad  # Guarda edad

    def set_correo(self, correo):  # Método para establecer correo
        if "@" not in correo:  # Valida que contenga @
            raise ClienteError("Correo inválido")  # Lanza error
        self.__correo = correo  # Guarda correo

    def get_nombre(self):  # Método getter del nombre
        return self.__nombre  # Retorna nombre

    def get_edad(self):  # Getter de edad
        return self.__edad  # Retorna edad

    def get_correo(self):  # Getter de correo
        return self.__correo  # Retorna correo

    def mostrar_info(self):  # Método para mostrar datos
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"  # Retorna string

#=======================================  # Separador
# PRUEBA DEL SISTEMA  # Simulación básica
#=======================================

if __name__ == "__main__":  # Verifica que se ejecute directamente

    print("=== PRUEBA CLIENTE ===")  # Mensaje en consola

    try:  # Bloque de prueba
        cliente1 = Cliente("Juan", 25, "juan@email.com")  # Crea cliente válido
        print(cliente1.mostrar_info())  # Muestra datos

        cliente2 = Cliente("", -5, "correo_invalido")  # Intenta crear cliente inválido

    except ClienteError as e:  # Captura error personalizado
        print("Error:", e)  # Muestra error en consola
        logger.error(e)  # Registra el error en el archivo log

#  SERVICIOS ESPECIALIZADOS

class ReservaSala(Servicio):
    """
    Servicio de reserva de salas de reuniones.
    Incluye capacidad máxima de personas como parámetro adicional.
    """

    def __init__(self, nombre: str, precio_hora: float,
                 capacidad: int, disponible: bool = True) -> None:
        super().__init__(nombre, precio_hora, disponible)
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ErrorServicio("La capacidad de la sala debe ser un entero positivo.")
        self.__capacidad = capacidad
        registrar_log("INFO", f"Servicio ReservaSala creado: {nombre}")

    def get_capacidad(self) -> int:
        return self.__capacidad

    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo base + cargo adicional de $5000 por hora si hay más de 20 personas."""
        if horas <= 0:
            raise ErrorDuracion("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ErrorServicio("El descuento debe estar entre 0 y 100.")
        cargo_extra = 5_000 if self.__capacidad > 20 else 0
        subtotal = (self._precio_hora + cargo_extra) * horas
        subtotal -= subtotal * (descuento / 100)
        if aplicar_iva:
            subtotal *= 1.19
        return round(subtotal, 2)

    def describir(self) -> str:
        return (f"Sala '{self._nombre}' | Capacidad: {self.__capacidad} personas "
                f"| Precio: ${self._precio_hora}/h")


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos tecnológicos.
    Incluye tipo de equipo y un depósito de garantía.
    """

    def __init__(self, nombre: str, precio_hora: float,
                 tipo_equipo: str, deposito: float = 0.0,
                 disponible: bool = True) -> None:
        super().__init__(nombre, precio_hora, disponible)
        if not tipo_equipo or not isinstance(tipo_equipo, str):
            raise ErrorServicio("El tipo de equipo no puede estar vacío.")
        if deposito < 0:
            raise ErrorServicio("El depósito no puede ser negativo.")
        self.__tipo_equipo = tipo_equipo
        self.__deposito = deposito
        registrar_log("INFO", f"Servicio AlquilerEquipo creado: {nombre}")

    def get_deposito(self) -> float:
        return self.__deposito

    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo = (precio_hora × horas + depósito) con descuento e IVA opcionales."""
        if horas <= 0:
            raise ErrorDuracion("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ErrorServicio("El descuento debe estar entre 0 y 100.")
        subtotal = self._precio_hora * horas + self.__deposito
        subtotal -= subtotal * (descuento / 100)
        if aplicar_iva:
            subtotal *= 1.19
        return round(subtotal, 2)

    def describir(self) -> str:
        return (f"Equipo '{self._nombre}' ({self.__tipo_equipo}) "
                f"| Precio: ${self._precio_hora}/h | Depósito: ${self.__deposito}")
