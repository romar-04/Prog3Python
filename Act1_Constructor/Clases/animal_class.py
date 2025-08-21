from datetime import date

class Animal:
    """
    Clase Animal que representa a una mascota con sus datos básicos
    """
    
    def __init__(self, nombre, peso, propietario, fecha_cumpleaños, fecha_ultima_vacuna):
        """
        Constructor de la clase Animal
        
        Args:
            nombre (str): Nombre del animal
            peso (float): Peso del animal en kg
            propietario (str): Nombre del propietario
            fecha_cumpleaños (date): Fecha de nacimiento del animal
            fecha_ultima_vacuna (date): Fecha de la última vacuna aplicada
        """
        self.__nombre = nombre
        self.__peso = peso
        self.__propietario = propietario
        self.__fecha_cumpleaños = fecha_cumpleaños
        self.__fecha_ultima_vacuna = fecha_ultima_vacuna
    
    # Métodos GET (Getters)
    def get_nombre(self):
        """Obtiene el nombre del animal"""
        return self.__nombre
    
    def get_peso(self):
        """Obtiene el peso del animal"""
        return self.__peso
    
    def get_propietario(self):
        """Obtiene el nombre del propietario"""
        return self.__propietario
    
    def get_fecha_cumpleaños(self):
        """Obtiene la fecha de cumpleaños del animal"""
        return self.__fecha_cumpleaños
    
    def get_fecha_ultima_vacuna(self):
        """Obtiene la fecha de la última vacuna"""
        return self.__fecha_ultima_vacuna
    
    # Métodos SET (Setters)
    def set_nombre(self, nombre):
        """Establece el nombre del animal"""
        self.__nombre = nombre
    
    def set_peso(self, peso):
        """Establece el peso del animal"""
        if peso > 0:
            self.__peso = peso
        else:
            raise ValueError("El peso debe ser mayor que cero")
    
    def set_propietario(self, propietario):
        """Establece el nombre del propietario"""
        self.__propietario = propietario
    
    def set_fecha_cumpleaños(self, fecha_cumpleaños):
        """Establece la fecha de cumpleaños del animal"""
        self.__fecha_cumpleaños = fecha_cumpleaños
    
    def set_fecha_ultima_vacuna(self, fecha_ultima_vacuna):
        """Establece la fecha de la última vacuna"""
        self.__fecha_ultima_vacuna = fecha_ultima_vacuna
    
    # Método adicional para mostrar información del animal
    def mostrar_info(self):
        """Muestra toda la información del animal"""
        return f"""
=== INFORMACIÓN DEL ANIMAL ===
Nombre: {self.__nombre}
Peso: {self.__peso} kg
Propietario: {self.__propietario}
Fecha de cumpleaños: {self.__fecha_cumpleaños}
Fecha última vacuna: {self.__fecha_ultima_vacuna}
==============================
        """