

from datetime import date

from Clases.animal import Animal

def main():
    """Función principal que demuestra el uso de la clase Animal"""
    
    print("=== DEMOSTRACIÓN DE LA CLASE ANIMAL ===\n")
    
    
    print("1. Creando animales...")
    
    
    animal1 = Animal(
        nombre="Max",
        peso=25.5,
        propietario="Juan Pérez",
        fecha_cumpleaños=date(2020, 3, 15),
        fecha_ultima_vacuna=date(2024, 1, 10)
    )
    
    
    animal2 = Animal(
        nombre="Luna",
        peso=4.2,
        propietario="María García",
        fecha_cumpleaños=date(2022, 7, 20),
        fecha_ultima_vacuna=date(2024, 2, 5)
    )
    
    
    animal3 = Animal(
        nombre="Rocky",
        peso=12.8,
        propietario="Carlos López",
        fecha_cumpleaños=date(2021, 11, 8),
        fecha_ultima_vacuna=date(2023, 12, 15)
    )
    
    
    print("2. Información inicial de los animales:")
    print(animal1.mostrar_info())
    print(animal2.mostrar_info())
    print(animal3.mostrar_info())
    
    
    print("3. Demostrando métodos GET:")
    print(f"Nombre del primer animal: {animal1.get_nombre()}")
    print(f"Peso del segundo animal: {animal2.get_peso()} kg")
    print(f"Propietario del tercer animal: {animal3.get_propietario()}")
    print(f"Cumpleaños de {animal1.get_nombre()}: {animal1.get_fecha_cumpleaños()}")
    print(f"Última vacuna de {animal2.get_nombre()}: {animal2.get_fecha_ultima_vacuna()}")
    
    
    print("\n4. Demostrando métodos SET (modificando datos):")
    
    
    animal1.set_peso(26.0)
    animal2.set_propietario("María Elena García")
    animal3.set_fecha_ultima_vacuna(date(2024, 8, 1))
    
    print("Datos modificados:")
    print(f"Nuevo peso de {animal1.get_nombre()}: {animal1.get_peso()} kg")
    print(f"Nuevo propietario de {animal2.get_nombre()}: {animal2.get_propietario()}")
    print(f"Nueva fecha de vacuna de {animal3.get_nombre()}: {animal3.get_fecha_ultima_vacuna()}")
    
    
    print("\n5. Información actualizada de los animales:")
    print(animal1.mostrar_info())
    print(animal2.mostrar_info())
    print(animal3.mostrar_info())
    
    # 
    print("6. Ejemplo de validación:")
    try:
        animal1.set_peso(-5)  
    except ValueError as e:
        print(f"Error capturado: {e}")
    
    print("\n=== FIN DE LA DEMOSTRACIÓN ===")

if __name__ == "__main__":
    main()
