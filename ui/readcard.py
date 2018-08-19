# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readcard.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_readCardDialog(object):
    def setupUi(self, readCardDialog):
        readCardDialog.setObjectName("readCardDialog")
        readCardDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        readCardDialog.resize(331, 128)
        self.vboxlayout = QtWidgets.QVBoxLayout(readCardDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(readCardDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.cardnoField = QtWidgets.QLineEdit(readCardDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.cardnoField.setFont(font)
        self.cardnoField.setObjectName("cardnoField")
        self.vboxlayout.addWidget(self.cardnoField)
        self.buttonBox = QtWidgets.QDialogButtonBox(readCardDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(readCardDialog)
        self.buttonBox.accepted.connect(readCardDialog.accept)
        self.buttonBox.rejected.connect(readCardDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(readCardDialog)

    def retranslateUi(self, readCardDialog):
        _translate = QtCore.QCoreApplication.translate
        readCardDialog.setWindowTitle(_translate("readCardDialog", "FVK: Indlæs kort"))
        self.label.setText(_translate("readCardDialog", "Indlæs kort:"))

