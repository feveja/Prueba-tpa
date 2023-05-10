import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Ejercicio 1 Seccion Practica Prueba Individual")
        self.setGeometry(100, 100, 600, 400)

        # Crear un widget central y un layout vertical
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Crear el título "Nombre de Usuario"
        title_label = QLabel("Nombre de Usuario")
        layout.addWidget(title_label)

        # Crear un layout horizontal para la imagen y la descripción
        image_layout = QHBoxLayout()

        # Cargar una imagen
        image_label = QLabel()
        pixmap = QPixmap("ruta/a/la/imagen.png")
        image_label.setPixmap(pixmap)
        image_layout.addWidget(image_label)

        # Crear una etiqueta para la descripción
        description_label = QLabel("Texto descripción del usuario")
        image_layout.addWidget(description_label)

        layout.addLayout(image_layout)

        # Crear un layout vertical para los atributos
        attributes_layout = QVBoxLayout()

        # Crear cuadros de texto para los atributos
        attributes_editors = []
        attribute_names = ["Atributo 1:", "Atributo 2:", "Atributo 3:", "Atributo 4:", "Atributo 5:", "Atributo 6:"]
        for attribute_name in attribute_names:
            attribute_label = QLabel(attribute_name)
            attributes_layout.addWidget(attribute_label)

            attribute_editor = QLineEdit()
            attributes_layout.addWidget(attribute_editor)

            attributes_editors.append(attribute_editor)

        layout.addLayout(attributes_layout)

        # Crear un layout horizontal para el botón
        button_layout = QHBoxLayout()

        # Crear el botón "OK"
        ok_button = QPushButton("OK")
        button_layout.addStretch()
        button_layout.addWidget(ok_button)

        layout.addLayout(button_layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
