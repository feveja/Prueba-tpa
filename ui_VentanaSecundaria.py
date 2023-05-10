# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaSecundariaOXRnjb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_VentanaSecundaria(object):
    def setupUi(self, VentanaSecundaria):
        if not VentanaSecundaria.objectName():
            VentanaSecundaria.setObjectName(u"VentanaSecundaria")
        VentanaSecundaria.resize(668, 311)
        self.verticalLayoutWidget = QWidget(VentanaSecundaria)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 661, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(VentanaSecundaria)

        QMetaObject.connectSlotsByName(VentanaSecundaria)
    # setupUi

    def retranslateUi(self, VentanaSecundaria):
        VentanaSecundaria.setWindowTitle(QCoreApplication.translate("VentanaSecundaria", u"VentanaSecundaria", None))
        self.label.setText(QCoreApplication.translate("VentanaSecundaria", u"Informaci\u00f3n Mascota", None))
        self.label_2.setText(QCoreApplication.translate("VentanaSecundaria", u"datos de la mascota", None))
        self.pushButton.setText(QCoreApplication.translate("VentanaSecundaria", u"OK", None))
    # retranslateUi

