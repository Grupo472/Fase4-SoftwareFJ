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
        self._id = id # Asigna el identificador único a un atributo de la instancia.
        self._fecha = datetime.now().strftime('%Y-%m-%d %H:%M') # Registra la fecha y hora de creación de la entidad en un formato legible.
    
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
# CLASE CLIENTE  
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

    def __init__(self, nombre: str, precio_base: float,
                 capacidad: int, disponible: bool = True) -> None:
        super().__init__(str(uuid.uuid4()), nombre, precio_base)# Genera un ID único para cada servicio de reserva de sala utilizando uuid4, lo que garantiza que cada sala tenga un identificador único en el sistema.
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ServicioError("La capacidad de la sala debe ser un entero positivo.") # Valida que la capacidad sea un número entero positivo, ya que una sala no puede tener una capacidad negativa o no entera.
        self.__capacidad = capacidad
        logger.info(f"Servicio ReservaSala creado: {nombre} con capacidad {capacidad} personas") # Registra en el logger la creación de un nuevo servicio de reserva de sala, incluyendo su nombre y capacidad, lo que ayuda a mantener un historial de los servicios disponibles en el sistema.

    def get_capacidad(self) -> int:
        return self.__capacidad
    def validar_parametros(self, horas, descuento=0): # Valida que la sala esté disponible, que las horas sean positivas y que el descuento esté entre 0 y 100.
        if not self._disponible:
            raise ServicioError(f"La sala '{self._nombre}' no está disponible.")# Valida que la sala esté disponible antes de permitir la reserva, lo que evita conflictos de reservas para la misma sala.
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.") # Valida que el número de horas para la reserva sea un valor positivo, ya que no tiene sentido reservar una sala por un tiempo negativo o cero.
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.") # Valida que el descuento aplicado a la reserva esté dentro del rango permitido (0% a 100%), lo que garantiza que el cálculo del costo sea correcto y no genere resultados negativos o excesivos.
    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo base + cargo adicional de $5000 por hora si hay más de 20 personas."""
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.")
        cargo_extra = 5_000 if self.__capacidad > 20 else 0
        subtotal = (self._precio_base + cargo_extra) * horas
        subtotal -= subtotal * (descuento / 100)
        if aplicar_iva:
            subtotal *= 1.19
        return round(subtotal, 2)

    def describir(self) -> str:
        return (f"Sala '{self._nombre}' | Capacidad: {self.__capacidad} personas "
                f"| Precio: ${self._precio_base}/h")
    def validar(self) -> bool:
        return True
class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos tecnológicos.
    Incluye tipo de equipo y un depósito de garantía.
    """

    def __init__(self, nombre: str, precio_base: float,
                 tipo_equipo: str, deposito: float = 0.0,
                 disponible: bool = True) -> None:
        super().__init__(str(uuid.uuid4()), nombre, precio_base)
        if not tipo_equipo or not isinstance(tipo_equipo, str):
            raise ServicioError("El tipo de equipo no puede estar vacío.")
        if deposito < 0:
            raise ServicioError("El depósito no puede ser negativo.")
        self.__tipo_equipo = tipo_equipo
        self.__deposito = deposito
        logger.info(f"Servicio AlquilerEquipo creado: {nombre} - Tipo: {tipo_equipo} - Depósito: ${deposito}")

    def get_deposito(self) -> float:
        return self.__deposito
    def validar_parametros(self, horas, descuento=0): # Valida que el equipo esté disponible, que las horas sean positivas y que el descuento esté entre 0 y 100.
        if not self._disponible:
            raise ServicioError(f"El equipo '{self._nombre}' no está disponible.") # Valida que el equipo esté disponible antes de permitir el alquiler.
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.") # Valida que el número de horas para el alquiler sea un valor positivo.
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.") # Valida que el descuento aplicado al alquiler esté dentro del rango permitido (0% a 100%).
    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """Costo = (precio_base × horas + depósito) con descuento e IVA opcionales."""
        if horas <= 0:
            raise ServicioError("Las horas deben ser un valor positivo.")
        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100.")
        subtotal = self._precio_base * horas + self.__deposito
        subtotal -= subtotal * (descuento / 100)
        if aplicar_iva:
            subtotal *= 1.19
        return round(subtotal, 2)

    def describir(self) -> str:
        return (f"Equipo '{self._nombre}' ({self.__tipo_equipo}) "

                f"| Precio: ${self._precio_base}/h | Depósito: ${self.__deposito}")
    def validar(self) -> bool:
        return True
# =============================
# CLASE ASESORIA ESPECIALIZADA
# =============================
class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría profesional por horas.
    """
    def __init__(self, nombre: str, precio_base: float,
                 especialidad: str, max_horas: int = 8):
        
        try:
            super().__init__(str(uuid.uuid4()), nombre, precio_base)
        except TypeError:
            super().__init__(nombre, precio_base)

        if not especialidad or not isinstance(especialidad, str):
            raise ServicioError("La especialidad no puede estar vacía.")

        if not isinstance(max_horas, int) or max_horas <= 0:
            raise ServicioError("El máximo de horas debe ser un entero positivo.")

        self.__especialidad = especialidad
        self.__max_horas = max_horas

        logger.info(f"Servicio AsesoriaEspecializada creado: {nombre} - Especialidad: {especialidad} - Máx Horas: {max_horas}")

    # ==========================
    # VALIDACIÓN (OBLIGATORIA)
    # ==========================
    def validar_parametros(self, horas, descuento):
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        if horas > self.__max_horas:
            raise ServicioError(
                f"No se permiten más de {self.__max_horas} horas de asesoría"
            )

        if not (0 <= descuento <= 100):
            raise ServicioError("El descuento debe estar entre 0 y 100")

    # ==========================
    # CÁLCULO (POLIMORFISMO)
    # ==========================
    def calcular_costo(self, horas=1, con_iva=False, descuento=0):
        self.validar_parametros(horas, descuento)

        recargo = 1.10  # 10% adicional por especialización

        subtotal = self._precio_base * horas * recargo

        return self.aplicar_descuento_iva(subtotal, con_iva, descuento)

    # ==========================
    # DESCRIPCIÓN
    # ==========================
    def describir(self):
        return (f"Asesoría '{self._nombre}' ({self.__especialidad}) "
                f"| Precio: ${self._precio_base}/h "
                f"| Máx horas: {self.__max_horas}")

    def validar(self) -> bool:
        return True   
       
# ==========================
# CLASE RESERVA
# ==========================
class Reserva(EntidadSistema):
   
    def __init__(self, cliente, servicio, duracion):
        # Validamos que cliente sea del tipo correcto
        super().__init__(str(uuid.uuid4()))  # Generamos un ID único para la reserva
        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        # Validamos que servicio sea una instancia válida de Servicio
        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        # Validamos que la duración sea numérica y positiva
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaError("Duración inválida")

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion

        # Estado inicial de la reserva
        self._estado = "pendiente"

        # Registro en logs
        logger.info("Reserva creada correctamente")
    def get_estado(self): # Método getter para obtener el estado actual de la reserva
        return self._estado # Retorna el estado actual de la reserva, que puede ser "pendiente", "confirmada", "procesada" o "cancelada". 
    # ==========================
    # CONFIRMAR RESERVA
    # ==========================
    def confirmar(self):
       
        # No se puede confirmar una reserva cancelada
        if self._estado in ["cancelada", "procesada", "confirmada"]:
            raise ReservaError(f"No se puede confirmar una reserva en estado '{self._estado}'")

        # Se verifica disponibilidad del servicio
        if not self._servicio.esta_disponible():
            raise ReservaError("Servicio no disponible")

        # Cambio de estado
        self._estado = "confirmada"

        # Registro en logs
        logger.info("Reserva confirmada")

    # ==========================
    # CANCELAR RESERVA
    # ==========================
    def cancelar(self):

        # No se puede cancelar si ya fue procesada o ya estaba cancelada
        if self._estado in ["procesada", "cancelada"]:
            raise ReservaError("No se puede cancelar esta reserva")

        # Cambio de estado
        self._estado = "cancelada"

        # Registro en logs
        logger.info("Reserva cancelada")

    # ==========================
    # PROCESAR RESERVA
    # ==========================
    def procesar(self):
    
        try:
            # No se puede procesar una reserva cancelada
            if self._estado == "cancelada":
                raise ReservaError("No se puede procesar una reserva cancelada")

            # Se calcula el costo usando el método del servicio
            # Se asume que el servicio implementa correctamente calcular_costo
            costo = self._servicio.calcular_costo(self._duracion)

        except Exception as e:
            # Se registra el error en logs
            logger.error(f"Error al procesar reserva: {e}")

            # Se relanza la excepción con encadenamiento
            raise ReservaError("Error al procesar la reserva") from e

        else:
            # Si todo salió bien, se actualiza el estado
            self._estado = "procesada"

            # Se registra el resultado
            logger.info(f"Costo calculado: {costo}")

            # Salida por consola (puede usarse para pruebas)
            print(f"Costo de la reserva: {costo}")

            # Se retorna el costo para uso posterior (tests, reportes, etc.)
            return costo

        finally:
            # Este bloque se ejecuta siempre, haya error o no
            logger.info("Proceso de reserva finalizado")
            
    def describir(self): # Método obligatorio heredado de la clase abstracta.
        return (f"Reserva [{self._id}] | "# ID único de la reserva
                f"Cliente: {self._cliente.get_nombre()} | " # Nombre del cliente asociado a la reserva
                f"Servicio: {self._servicio.get_nombre()} | " # Nombre del servicio reservado
                f"Duración: {self._duracion}h | Estado: {self._estado}") #  Duración de la reserva y su estado actual (pendiente, confirmada, procesada, cancelada)

    def validar(self) -> bool:# Método obligatorio heredado de la clase abstracta.
        return self._estado in ["pendiente", "confirmada", "procesada", "cancelada"] # Valida que el estado de la reserva sea uno de los estados permitidos, lo que indica que la reserva está en un estado correcto.
#==============================================================================
# CLASE SISTEMA GESTION
#==============================================================================

class SistemaGestion:
    def __init__(self):
        self._clientes  = []  # Lista interna de clientes registrados
        self._servicios = []  # Lista interna de servicios disponibles
        self._reservas  = []  # Lista interna de reservas creadas
        logger.info("[SISTEMA] Software FJ iniciado correctamente")

    # ------------------------------------------------------------------
    # GESTIÓN DE CLIENTES
    # ------------------------------------------------------------------

    def registrar_cliente(self, id, nombre, correo, telefono):
   
        try:
            cliente = Cliente(id, nombre, correo, telefono)
        except ClienteError as e:
            print(f"  {e}")
            return None
        else:
            self._clientes.append(cliente)
            print(f" Cliente registrado: {cliente.get_nombre()}")
            return cliente
        finally:
            logger.info("[SISTEMA] Intento de registro de cliente finalizado")

    def buscar_cliente(self, id):
    
        for cliente in self._clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    def listar_clientes(self):
        """Muestra todos los clientes registrados en el sistema."""
        if not self._clientes:
            print(" No hay clientes registrados.")
            return
        print("  Clientes registrados:")
        for cliente in self._clientes:
            print(f"    - {cliente.describir()}")

    # ------------------------------------------------------------------
    # GESTIÓN DE SERVICIOS
    # ------------------------------------------------------------------

    def agregar_servicio(self, servicio):

        try:
            if not isinstance(servicio, Servicio):
                raise ServicioError("El objeto proporcionado no es un Servicio válido.")
            self._servicios.append(servicio)
            print(f"   Servicio agregado: {servicio.get_nombre()}")
            return servicio
        except ServicioError as e:
            print(f"   {e}")
            return None

    def buscar_servicio(self, id):

        for servicio in self._servicios:
            if servicio.get_id() == id:
                return servicio
        return None

    def listar_servicios(self):
        if not self._servicios:
            print("  No hay servicios registrados.")
            return
        print("  Servicios disponibles:")
        for servicio in self._servicios:
            print(f"    - {servicio.describir()}")

    # ------------------------------------------------------------------
    # GESTIÓN DE RESERVAS
    # ------------------------------------------------------------------

    def crear_reserva(self, cliente, servicio, duracion):

        try:
            reserva = Reserva(cliente, servicio, duracion)
        except ReservaError as e:
            print(f"   {e}")
            return None
        else:
            self._reservas.append(reserva)
            print(f"   Reserva creada: {reserva.describir()}")
            return reserva

    def buscar_reserva(self, id):

        for reserva in self._reservas:
            if reserva.get_id() == id:
                return reserva
        return None

    def listar_reservas(self):
        if not self._reservas:
            print("  No hay reservas registradas.")
            return
        print("  Reservas registradas:")
        for reserva in self._reservas:
            print(f"    - {reserva.describir()}")

    def listar_reservas_por_estado(self, estado):

        filtradas = [r for r in self._reservas if r.get_estado() == estado]
        if not filtradas:
            print(f"  No hay reservas con estado '{estado}'.")
            return
        print(f"  Reservas con estado '{estado}':")
        for reserva in filtradas:
            print(f"    - {reserva.describir()}")

            f"| Precio: ${self._precio_base}/h | Depósito: ${self.__deposito}"
    def validar(self) -> bool:
        return True

#=============================================================================
# SIMULACIÓN — 10 OPERACIONES DEL SISTEMA
#==============================================================================

def main(): # Función principal que simula el funcionamiento del sistema de gestión de clientes, servicios y reservas demostrando la creación de clientes, servicios, reservas y el manejo de errores a través de excepciones personalizadas.
    print("=" * 65)
    print("   SISTEMA DE GESTIÓN - SOFTWARE FJ")
    print("   Fase 4 - Programación 213023 - UNAD - Grupo 472")
    print("   Simulación de 10 operaciones")
    print("=" * 65)

    sistema = SistemaGestion() # Instancia del sistema de gestión, que se utilizará para registrar clientes, agregar servicios y crear reservas a lo largo de la simulación.
    # ------------------------------------------------------------------
    # OP 1 — Registro INVÁLIDO: email sin formato correcto
    print("\n[OP 1] Registro inválido — email sin formato correcto:")
    sistema.registrar_cliente("C001", "Pedro Gomez", "correomal", "3001234567")

    # ------------------------------------------------------------------
    # OP 2 — Registro VÁLIDO de primer cliente
    print("\n[OP 2] Registro válido — primer cliente:")
    c1 = sistema.registrar_cliente(
        "C002", "Juan Perez", "juan@email.com", "3001234567"
    )

    # ------------------------------------------------------------------
    # OP 3 — Registro INVÁLIDO: nombre vacío
    print("\n[OP 3] Registro inválido — nombre vacío:")
    sistema.registrar_cliente("C003", "", "test@email.com", "3009999999")

    # ------------------------------------------------------------------
    # OP 4 — Registro VÁLIDO de segundo cliente
    print("\n[OP 4] Registro válido — segundo cliente:")
    c2 = sistema.registrar_cliente(
        "C004", "Carlos Ruiz", "carlos@email.com", "3007654321"
    )

    # ------------------------------------------------------------------
    # OP 5 — Crear los tres servicios y demostrar polimorfismo en describir()
    print("\n[OP 5] Crear servicios — polimorfismo en describir():") 
    sala = asesoria = equipo = None # Inicializamos las variables para evitar referencias a variables no definidas en caso de error
    try:
        sala     = ReservaSala("Sala Innovación", 50_000, 15) # Servicio de reserva de sala con capacidad para 15 personas
        asesoria = AsesoriaEspecializada("Asesoría Python", 80_000, "Dr. García") # Servicio de asesoría especializada en Python con un precio base de 80,000 por hora y una especialidad a cargo del Dr. García
        equipo   = AlquilerEquipo("Portátiles HP", 15_000, "Laptop", 50_000) # Servicio de alquiler de equipos tecnológicos para portátiles HP con un precio base de 15,000 por hora y un depósito de garantía de 50,000

        sistema.agregar_servicio(sala) # Agrega el servicio de reserva de sala al sistema, lo que permite que los clientes puedan reservar esta sala para sus reuniones o eventos.
        sistema.agregar_servicio(asesoria) # Agrega el servicio de asesoría especializada al sistema, lo que permite que los clientes puedan solicitar asesorías profesionales en diferentes áreas de especialización.
        sistema.agregar_servicio(equipo) # Agrega el servicio de alquiler de equipos tecnológicos al sistema, lo que permite que los clientes puedan alquilar diferentes tipos de equipos para sus necesidades tecnológicas.

        print("\n  Polimorfismo — mismo método describir(), tres resultados distintos:")
        for s in [sala, asesoria, equipo]:
            print(f"  → {s.describir()}")

    except ServicioError as e:
        print(f" {e}")

    # ------------------------------------------------------------------
    # OP 6 — Reserva INVÁLIDA: asesoría supera límite de horas
    print("\n[OP 6] Reserva inválida — asesoría supera límite de horas (máx 4h):") 
    if c1 and asesoria: 
        r_invalida = sistema.crear_reserva(c1, asesoria, 6)  # 6h > HORAS_MAX=4
        if r_invalida:
            try:
                r_invalida.procesar()
            except ReservaError as e:
                print(f"   Reserva bloqueada: {e}")

    # ------------------------------------------------------------------
    # OP 7 — Reserva INVÁLIDA: servicio no disponible
    print("\n[OP 7] Reserva inválida — servicio marcado como no disponible:")
    if c1 and sala:
        sala.set_disponible(False)
        sistema.crear_reserva(c1, sala, 3)
        sala.set_disponible(True)  # restaurar para las siguientes ops

    # ------------------------------------------------------------------
    # OP 8 — Reserva VÁLIDA con IVA y descuento
    print("\n[OP 8] Reserva válida — sala 3h con IVA 19% y descuento 10%:")
    r1 = None
    if c1 and sala:
        r1 = sistema.crear_reserva(c1, sala, 3)
        if r1:
            try:
                costo = r1.confirmar(con_iva=True, descuento=10)
                print(f"   Reserva confirmada — Costo final: ${costo:,.2f}")
            except ReservaError as e:
                print(f"   {e}")

    # ------------------------------------------------------------------
    # OP 9 — Operación NO PERMITIDA: confirmar una reserva ya confirmada
    print("\n[OP 9] Operación no permitida — confirmar reserva ya confirmada:")
    if r1:
        try:
            r1.confirmar()
        except ReservaError as e:
            print(f"  Operación bloqueada: {e}")

    # ------------------------------------------------------------------
    # OP 10 — Operación NO PERMITIDA: cancelar una reserva ya cancelada
    print("\n[OP 10] Operación no permitida — cancelar reserva dos veces:")
    r2 = None
    if c2 and equipo:
        r2 = sistema.crear_reserva(c2, equipo, 2)
        if r2:
            try:
                r2.cancelar()
                print("  Primera cancelación exitosa")
                r2.cancelar()  # segundo intento — debe fallar controladamente
            except ReservaError as e:
                print(f"  Segunda cancelación bloqueada: {e}")

# Simulación completa
    print("\n" + "=" * 65)
    print("   Simulación completada — sistema estable en todas las operaciones")
    print("   Registro completo en: logs/sistema.log")
    print("=" * 65)

# Ejecutar la función principal para iniciar la simulación del sistema de gestión de clientes, servicios y reservas, demostrando las operaciones y el manejo de errores a través de excepciones personalizadas. 
if __name__ == "__main__":
    main()