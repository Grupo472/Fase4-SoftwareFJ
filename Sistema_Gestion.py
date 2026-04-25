#=======================================
#  Sistema Integral de Gestión de Clientes, Servicios y Reservas
#  Fase 4 - Programación 213023 - UNAD - Grupo 472
# Desarrollado por: 
# Edisson Ferney Parrado Reyes
# Alexandra Tautiva Betancur
# Daniel Eduardo Caro Rodriguez
# Hugo Enrique Florez Granados
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
