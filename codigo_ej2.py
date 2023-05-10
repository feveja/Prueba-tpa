import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)


    def guardar_mascota(self):
        nombre = self.lineEditNombre.text()
        especie = self.lineEditEspecie.text()
        edad = int(self.lineEditEdad.text())
        peso = float(self.lineEditPeso.text())

        mascota = Mascota(nombre, especie, edad, peso)
        print("Mascota guardada:", mascota)
        
        # Limpia los campos de entrada después de guardar
        self.lineEditNombre.clear()
        self.lineEditEspecie.clear()
        self.lineEditEdad.clear()
        self.lineEditPeso.clear()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    vista = Ventana()
    vista.show()
    app.exec()