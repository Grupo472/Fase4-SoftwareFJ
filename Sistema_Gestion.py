#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
#==============================================================================
# Se importan las librerías necesarias para el funcionamiento del sistema, incluyendo re para expresiones regulares, 
# uuid para generación de identificadores únicos, logging para registro de eventos, 
# os para operaciones del sistema operativo, abc para clases abstractas y datetime para manejo de fechas y horas.
#==============================================================================
import re
import uuid
import logging
import os
from abc import ABC, abstractmethod
from datetime import datetime
#=======================================
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
