# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edititems.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditItemsForm(object):
    def setupUi(self, EditItemsForm):
        EditItemsForm.setObjectName("EditItemsForm")
        EditItemsForm.resize(373, 340)
        self.vboxlayout = QtWidgets.QVBoxLayout(EditItemsForm)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(EditItemsForm)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.itemsView = QtWidgets.QTableView(EditItemsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.itemsView.sizePolicy().hasHeightForWidth())
        self.itemsView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.itemsView.setFont(font)
        self.itemsView.setAlternatingRowColors(True)
        self.itemsView.setShowGrid(False)
        self.itemsView.setSortingEnabled(True)
        self.itemsView.setObjectName("itemsView")
        self.vboxlayout.addWidget(self.itemsView)
        self.widget = QtWidgets.QWidget(EditItemsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.widget)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.addButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.hboxlayout.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.hboxlayout.addWidget(self.removeButton)
        self.vboxlayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(EditItemsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.hboxlayout1 = QtWidgets.QHBoxLayout(self.widget_3)
        self.hboxlayout1.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout1.addWidget(self.closeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addWidget(self.widget_3)

        self.retranslateUi(EditItemsForm)
        QtCore.QMetaObject.connectSlotsByName(EditItemsForm)

    def retranslateUi(self, EditItemsForm):
        _translate = QtCore.QCoreApplication.translate
        EditItemsForm.setWindowTitle(_translate("EditItemsForm", "Ret varer"))
        self.label.setText(_translate("EditItemsForm", "Ret varer"))
        self.addButton.setText(_translate("EditItemsForm", "&Tilføj ny vare"))
        self.removeButton.setText(_translate("EditItemsForm", "&Fjern vare"))
        self.closeButton.setText(_translate("EditItemsForm", "&Luk"))

