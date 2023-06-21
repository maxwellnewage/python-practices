"""
Clase abstracta Vehicle
"""
class Vehicle:
    def stop_engine() -> str:
        """Metodo para detener el motor
        :return str
        """
        pass

    def run_engine() -> str:
        """Metodo para arrancar el motor
        :return str
        """
        pass

"""
Clase Car 
"""
class Car(Vehicle):
    def stop_engine() -> str:
        return "stopping..."

    def run_engine() -> str:
        return "starting..."