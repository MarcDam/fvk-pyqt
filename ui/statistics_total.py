# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_total.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticsTotal(object):
    def setupUi(self, StatisticsTotal):
        StatisticsTotal.setObjectName("StatisticsTotal")
        StatisticsTotal.resize(555, 385)
        self.gridlayout = QtWidgets.QGridLayout(StatisticsTotal)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(StatisticsTotal)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(StatisticsTotal)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.totalView = QtWidgets.QTreeView(StatisticsTotal)
        self.totalView.setObjectName("totalView")
        self.gridlayout.addWidget(self.totalView, 1, 0, 1, 1)
        self.itemView = QtWidgets.QTreeView(StatisticsTotal)
        self.itemView.setObjectName("itemView")
        self.gridlayout.addWidget(self.itemView, 1, 1, 1, 1)

        self.retranslateUi(StatisticsTotal)
        QtCore.QMetaObject.connectSlotsByName(StatisticsTotal)

    def retranslateUi(self, StatisticsTotal):
        _translate = QtCore.QCoreApplication.translate
        StatisticsTotal.setWindowTitle(_translate("StatisticsTotal", "Form"))
        self.label.setText(_translate("StatisticsTotal", "Total:"))
        self.label_2.setText(_translate("StatisticsTotal", "Pr. vare:"))

