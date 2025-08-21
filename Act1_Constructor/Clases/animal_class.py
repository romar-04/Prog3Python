from datetime import date

class Animal:
    
    def __init__(self, nombre, peso, propietario, fecha_cumpleaños, fecha_ultima_vacuna):
        
        self.__nombre = nombre
        self.__peso = peso
        self.__propietario = propietario
        self.__fecha_cumpleaños = fecha_cumpleaños
        self.__fecha_ultima_vacuna = fecha_ultima_vacuna
    
    def get_nombre(self):
       
        return self.__nombre
    
    def get_peso(self):
        
        return self.__peso
    
    def get_propietario(self):
        
        return self.__propietario
    
    def get_fecha_cumpleaños(self):
        
        return self.__fecha_cumpleaños
    
    def get_fecha_ultima_vacuna(self):
        
        return self.__fecha_ultima_vacuna
    
    
    def set_nombre(self, nombre):
        
        self.__nombre = nombre
    
    def set_peso(self, peso):
        
        if peso > 0:
            self.__peso = peso
        else:
            raise ValueError("El peso debe ser mayor que cero")
    
    def set_propietario(self, propietario):
        
        self.__propietario = propietario
    
    def set_fecha_cumpleaños(self, fecha_cumpleaños):
        
        self.__fecha_cumpleaños = fecha_cumpleaños
    
    def set_fecha_ultima_vacuna(self, fecha_ultima_vacuna):
        
        self.__fecha_ultima_vacuna = fecha_ultima_vacuna
    
    
    def mostrar_info(self):
        
        return 
=== INFORMACIÓN DEL ANIMAL ===
Nombre: {self.__nombre}
Peso: {self.__peso} kg
Propietario: {self.__propietario}
Fecha de cumpleaños: {self.__fecha_cumpleaños}
Fecha última vacuna: {self.__fecha_ultima_vacuna}
