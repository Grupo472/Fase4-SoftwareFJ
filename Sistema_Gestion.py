#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
# Hugo Enrique Florez Granados
#=======================================

import datetime
from abc import ABC, abstractmethod

# ─────────────────────────────────────────────
#  UTILIDAD: Registro de logs
# ─────────────────────────────────────────────
LOG_FILE = "logs.txt"

def registrar_log(tipo: str, mensaje: str) -> None:
    """Registra un evento o error en el archivo de logs."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] [{tipo.upper()}] {mensaje}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except OSError as e:
        print(f"  [ADVERTENCIA] No se pudo escribir en logs: {e}")


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



#  CLASE ABSTRACTA: Servicio
# ─────────────────────────────────────────────
class Servicio(EntidadSistema, ABC):
    """
    Clase abstracta que representa un servicio ofrecido por Software FJ.
    Las subclases deben implementar calcular_costo y describir.
    """

    def __init__(self, nombre: str, precio_hora: float, disponible: bool = True) -> None:
        if not nombre or not isinstance(nombre, str):
            raise ErrorServicio("El nombre del servicio no puede estar vacío.")
        if not isinstance(precio_hora, (int, float)) or precio_hora < 0:
            raise ErrorServicio("El precio por hora debe ser un número no negativo.")
        self._nombre = nombre
        self._precio_hora = float(precio_hora)
        self._disponible = disponible

    def get_nombre(self) -> str:
        return self._nombre

    def get_precio_hora(self) -> float:
        return self._precio_hora

    def esta_disponible(self) -> bool:
        return self._disponible

    def set_disponible(self, estado: bool) -> None:
        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, horas: float, descuento: float = 0.0,
                       aplicar_iva: bool = False) -> float:
        """
        Calcula el costo del servicio.
        Método sobrecargado mediante parámetros opcionales:
          - horas: duración en horas (requerido)
          - descuento: porcentaje de descuento 0-100 (opcional, defecto 0)
          - aplicar_iva: si se aplica IVA del 19% (opcional, defecto False)
        """
        pass

    def validar(self) -> bool:
        return self._precio_hora >= 0 and bool(self._nombre)

    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self.__class__.__name__}] {self._nombre} | ${self._precio_hora}/h | {estado}"


# ─────────────────────────────────────────────
#  SERVICIOS ESPECIALIZADOS
# ─────────────────────────────────────────────
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

