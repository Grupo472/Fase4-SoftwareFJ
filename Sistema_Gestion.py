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
    def __init__(self, id): # Constructor que recibe un identificador único para la entidad y lo asigna a un atributo, además de registrar la fecha de creación.
        self.id = id # Asigna el identificador único a un atributo de la instancia.
        self.fecha = datetime.now().strftime('%Y-%m-%d %H:%M') # Registra la fecha y hora de creación de la entidad en un formato legible.
    
    def get_id(self): # Método getter para obtener el identificador de la entidad.
        return self._id # Retorna el identificador de la entidad.
    
    def get_fecha(self): # Método getter para obtener la fecha de creación de la entidad.
        return self._fecha # Retorna la fecha de creación de la entidad.

    @abstractmethod
    def describir(self):
        """Retorna una descripción textual de la entidad."""
        pass

    @abstractmethod
    def validar(self) -> bool:
        """Valida que la entidad esté en un estado correcto."""
        pass

    
#==============================================================================
# CLASE CLIENTE  # Tu rama integracion corregida acorde a revicion no uso entidadbase pues me genera error
#==============================================================================

class Cliente(EntidadSistema):  # Define la clase Cliente heredando de EntidadBase para obtener id y fecha automáticamente

    def __init__(self, id, nombre, correo, telefono):  # Constructor que recibe id, nombre, correo y teléfono
        super().__init__(id)  # Llama al constructor de la clase padre para inicializar id y fecha de creación

        self.set_nombre(nombre)  # Llama al método setter para validar y asignar el nombre
        self.set_correo(correo)  # Llama al setter para validar el correo con expresión regular
        self.set_telefono(telefono)  # Llama al setter para validar y asignar el teléfono

    # VALIDACIÓN NOMBRE
    # ============================

    def set_nombre(self, nombre):  # Método para establecer el nombre del cliente
        if not isinstance(nombre, str) or nombre.strip() == "":  # Verifica que el nombre sea texto y no esté vacío
            raise ClienteError("El nombre no puede estar vacío")  # Lanza excepción personalizada si la validación falla
        self.__nombre = nombre  # Guarda el nombre como atributo privado

    def get_nombre(self):  # Método getter para obtener el nombre
        return self.__nombre  # Retorna el nombre almacenado

    # VALIDACIÓN CORREO (REGEX)
    # ============================

    def set_correo(self, correo):  # Método para establecer el correo electrónico
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"  # Define la expresión regular para validar el formato de email
        if not re.match(patron, correo):  # Verifica si el correo cumple el patrón definido
            raise ClienteError("Correo inválido")  # Lanza excepción si el correo no es válido
        self.__correo = correo  # Guarda el correo como atributo privado

    def get_correo(self):  # Método getter del correo
        return self.__correo  # Retorna el correo almacenado

    # VALIDACIÓN TELÉFONO
    # ============================

    def set_telefono(self, telefono):  # Método para establecer el número de teléfono
        if not telefono.isdigit() or len(telefono) < 7:  # Verifica que tenga solo números y mínimo 7 dígitos
            raise ClienteError("El teléfono debe tener al menos 7 dígitos")  # Lanza excepción si no cumple la validación
        self.__telefono = telefono  # Guarda el teléfono como atributo privado

    def get_telefono(self):  # Método getter del teléfono
        return self.__telefono  # Retorna el teléfono almacenado

    # MÉTODOS OBLIGATORIOS
    # ============================

    def describir(self):  # Método obligatorio heredado de la clase abstracta
        return f"Cliente {self.__nombre} - Correo: {self.__correo} - Teléfono: {self.__telefono}"  # Retorna una descripción del cliente

    def validar(self):  # Método obligatorio heredado de la clase abstracta
        return True  # Retorna True indicando que el cliente es válido (puede ampliarse con más validaciones)


    # MÉTODO ADICIONAL
    # ============================

    def mostrar_info(self):  # Método para mostrar la información completa del cliente
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}, Teléfono: {self.__telefono}"  # Retorna un string con los datos del cliente

#==============================================================================
# CLASE SERVICIO
#==============================================================================
class Servicio(EntidadSistema, ABC):
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
            raise ServicioError("La capacidad de la sala debe ser un entero positivo.") # Valida que la capacidad sea un número entero positivo, ya que una sala no puede tener una capacidad negativa o no entera.
        self.__capacidad = capacidad
        logger.info ("INFO", f"Servicio ReservaSala creado: {nombre}")

    def get_capacidad(self) -> int:
        return self.__capacidad

    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo base + cargo adicional de $5000 por hora si hay más de 20 personas."""
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.")
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
            raise ServicioError("El tipo de equipo no puede estar vacío.")
        if deposito < 0:
            raise ServicioError("El depósito no puede ser negativo.")
        self.__tipo_equipo = tipo_equipo
        self.__deposito = deposito
        logger.info ("INFO", f"Servicio AlquilerEquipo creado: {nombre}")

    def get_deposito(self) -> float:
        return self.__deposito

    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo = (precio_hora × horas + depósito) con descuento e IVA opcionales."""
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.")
        subtotal = self._precio_hora * horas + self.__deposito
        subtotal -= subtotal * (descuento / 100)
        if aplicar_iva:
            subtotal *= 1.19
        return round(subtotal, 2)

    def describir(self) -> str:
        return (f"Equipo '{self._nombre}' ({self.__tipo_equipo}) "
                f"| Precio: ${self._precio_hora}/h | Depósito: ${self.__deposito}")
        
# ==========================
# CLASE RESERVA
# ==========================
class Reserva(EntidadSistema):
   
    def __init__(self, cliente, servicio, duracion):
        # Validamos que cliente sea del tipo correcto
        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        # Validamos que servicio sea una instancia válida de Servicio
        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        # Validamos que la duración sea numérica y positiva
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Estado inicial de la reserva
        self.estado = "pendiente"

        # Registro en logs
        logger.info("Reserva creada correctamente")

    # ==========================
    # CONFIRMAR RESERVA
    # ==========================
    def confirmar(self):
       
        # No se puede confirmar una reserva cancelada
        if self.estado == "cancelada":
            raise ReservaError("No se puede confirmar una reserva cancelada")

        # Se verifica disponibilidad del servicio
        if not self.servicio.esta_disponible():
            raise ReservaError("Servicio no disponible")

        # Cambio de estado
        self.estado = "confirmada"

        # Registro en logs
        logger.info("Reserva confirmada")

    # ==========================
    # CANCELAR RESERVA
    # ==========================
    def cancelar(self):

        # No se puede cancelar si ya fue procesada o ya estaba cancelada
        if self.estado in ["procesada", "cancelada"]:
            raise ReservaError("No se puede cancelar esta reserva")

        # Cambio de estado
        self.estado = "cancelada"

        # Registro en logs
        logger.info("Reserva cancelada")

    # ==========================
    # PROCESAR RESERVA
    # ==========================
    def procesar(self):
    
        try:
            # No se puede procesar una reserva cancelada
            if self.estado == "cancelada":
                raise ReservaError("No se puede procesar una reserva cancelada")

            # Se calcula el costo usando el método del servicio
            # Se asume que el servicio implementa correctamente calcular_costo
            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as e:
            # Se registra el error en logs
            logger.error(f"Error al procesar reserva: {e}")

            # Se relanza la excepción con encadenamiento
            raise ReservaError("Error al procesar la reserva") from e

        else:
            # Si todo salió bien, se actualiza el estado
            self.estado = "procesada"

            # Se registra el resultado
            logger.info(f"Costo calculado: {costo}")

            # Salida por consola (puede usarse para pruebas)
            print(f"Costo de la reserva: {costo}")

            # Se retorna el costo para uso posterior (tests, reportes, etc.)
            return costo

        finally:
            # Este bloque se ejecuta siempre, haya error o no
            logger.info("Proceso de reserva finalizado")
