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
#===============================================================================

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
class ErrorSistema(Exception): # Define una clase de excepción personalizada para el sistema, que hereda de la clase base Exception.
    def __init__(self, mensaje): # Constructor que recibe un mensaje de error y lo pasa a la clase base Exception, además de registrar el error en el logger.
        super().__init__(mensaje) # Llama al constructor de la clase base Exception para inicializar la excepción con el mensaje proporcionado.
        logger.error(f"[ERROR] {mensaje}") # Registra el mensaje de error en el logger con un nivel de error, lo que permite mantener un registro de los errores que ocurren en el sistema.

class ClienteError(ErrorSistema): # Define una clase de excepción personalizada para errores relacionados con los clientes, que hereda de ErrorSistema.
    def __init__(self, mensaje): # Constructor que recibe un mensaje de error específico para clientes y lo formatea antes de pasarlo al constructor de ErrorSistema.
        super().__init__(f"ClienteError: {mensaje}") # Llama al constructor de ErrorSistema con un mensaje formateado que indica que se trata de un error relacionado con los clientes, lo que ayuda a identificar el origen del error en los logs.

class ServicioError(ErrorSistema): # Define una clase de excepción personalizada para errores relacionados con los servicios, que hereda de ErrorSistema.
    def __init__(self, mensaje): # Constructor que recibe un mensaje de error específico para servicios y lo formatea antes de pasarlo al constructor de ErrorSistema.
        super().__init__(f"ServicioError: {mensaje}") # Llama al constructor de ErrorSistema con un mensaje formateado que indica que se trata de un error relacionado con los servicios, lo que ayuda a identificar el origen del error en los logs.

class ReservaError(ErrorSistema): # Define una clase de excepción personalizada para errores relacionados con las reservas, que hereda de ErrorSistema.
    def __init__(self, mensaje): # Constructor que recibe un mensaje de error específico para reservas y lo formatea antes de pasarlo al constructor de ErrorSistema.
        super().__init__(f"ReservaError: {mensaje}") # Llama al constructor de ErrorSistema con un mensaje formateado que indica que se trata de un error relacionado con las reservas, lo que ayuda a identificar el origen del error en los logs.


#==============================================================================
# DEFINICION ENTIDAD BASE
#==============================================================================
class EntidadSistema(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Define la interfaz común: describir y validar.
    """

    def __init__(self, id: int, fecha_creacion: str):
        self.id = id
        self.fecha_creacion = fecha_creacion

    @abstractmethod
    def describir(self):
        """Retorna una descripción textual de la entidad."""
        pass

    @abstractmethod
    def validar(self) -> bool:
        """Valida que la entidad esté en un estado correcto."""
        pass

#==============================================================================
# CLASE CLIENTE 
#==============================================================================
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

#==============================================================================
# CLASE SERVICIO
#==============================================================================
lass Servicio(EntidadBase, ABC):
    """Clase abstracta base para los servicios de Software FJ."""
 
    def __init__(self, id, nombre, precio_base): # id es para EntidadBase
        super().__init__(id)
        if not nombre or not nombre.strip():
            raise ServicioError('El nombre no puede estar vacío')
        if precio_base <= 0:
            raise ServicioError('El precio debe ser mayor a cero')
        self._nombre      = nombre.strip()
        self._precio_base = precio_base
        self._disponible  = True
 
    def get_nombre(self):       return self._nombre
    def get_precio(self):       return self._precio_base
    def esta_disponible(self):  return self._disponible
    def set_disponible(self, estado): self._disponible = estado
 
    # ── Métodos abstractos (polimorfismo) ──────────────
    @abstractmethod
    def validar_parametros(self, horas, descuento): pass
 
    @abstractmethod
    def calcular_costo(self, horas=1, con_iva=False, descuento=0): pass
 
    @abstractmethod
    def describir(self): pass
 
    # ── Método auxiliar compartido ─────────────────────
    def aplicar_descuento_iva(self, subtotal, con_iva, descuento):
        if descuento < 0 or descuento > 100:
            raise ServicioError(f'Descuento {descuento}% fuera de rango')
        total = subtotal * (1 - descuento / 100)
        if con_iva:
            total *= 1.19
        return round(total, 2)

#==============================================================================
#  SERVICIOS ESPECIALIZADOS
#==============================================================================
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
