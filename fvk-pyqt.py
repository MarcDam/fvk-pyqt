#!/usr/bin/python3

###
# This file is part of the PyQt NatCafé FVK-system.
# Copyright (C) 2018 Marc John Bordier Dam
# Copyright (C) 2007 Toke Høiland-Jørgensen
# 
# PyQt NatCafé FVK-system is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# PyQt NatCafé FVK-system is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 ###

version = 1

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtCore

from ui import addmoney, adduser, edititems, editusers, mainwindow, readcard, statistics, statistics_total

class AddMoney(QDialog):
    def __init__(self):
        super(AddMoney, self).__init__()
        
        self.ui = addmoney.Ui_AddMoneyForm()
        self.ui.setupUi(self)
        
        self.setModal(True)
        
class AddUser(QDialog):
    def __init__(self):
        super(AddUser, self).__init__()
        
        self.ui = adduser.Ui_AddUserForm()
        self.ui.setupUi(self)
        
        self.setModal(True)

class EditItems(QDialog):
    def __init__(self):
        super(EditItems, self).__init__()
        
        self.ui = edititems.Ui_EditItemsForm()
        self.ui.setupUi(self)
        
        self.setModal(True)

class EditUsers(QDialog):
    def __init__(self):
        super(EditUsers, self).__init__()
        
        self.ui = editusers.Ui_EditUsersForm()
        self.ui.setupUi(self)
        
        self.setModal(True)
        
class ReadCard(QDialog):
    def __init__(self):
        super(ReadCard, self).__init__()
        
        self.ui = readcard.Ui_readCardDialog()
        self.ui.setupUi(self)
        
        self.setModal(True)

class Statistics(QDialog):
    def __init__(self):
        super(Statistics, self).__init__()
        
        self.ui = statistics.Ui_StatisticsForm()
        self.ui.setupUi(self)
        
        self.setModal(True)

class FVK(QMainWindow):
    def __init__(self, parent=None):
        super(FVK, self).__init__(parent)

        # Setup the GUI
        self.ui = mainwindow.Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        # Main window buttons
        self.ui.addButton.clicked.connect(self.addButton)
        self.ui.removeButton.clicked.connect(self.removeButton)
        self.ui.doOrderButton.clicked.connect(self.doOrderButton)
        self.ui.addMoneyButton.clicked.connect(self.addMoneyButton)
        
        # Menu items
        self.ui.actionAddUser.triggered.connect(self.addUser)
        self.ui.actionEditItems.triggered.connect(self.editItems)
        self.ui.actionStatistics.triggered.connect(self.statistics)
        self.statisticsDialog = Statistics()
        self.ui.actionEditUsers.triggered.connect(self.editUsers)
        self.ui.actionLoadUser.triggered.connect(self.loadUser)
        self.ui.actionAbout.triggered.connect(self.about)
        
    ### Functions called by clicked buttons in the main window ###
    def addButton(self, checked):
        print(self.ui.addButton.text())
        
    def removeButton(self, checked):
        print(self.ui.removeButton.text())
        
    def doOrderButton(self, checked):
        print(self.ui.doOrderButton.text())
        
    def addMoneyButton(self, checked):
        print(self.ui.addMoneyButton.text())
        self.addMoneyDialog = AddMoney()
        self.addMoneyDialog.show()
        
    ### Functions called by triggered menu items in the main window ###
    def addUser(self, checked):
        print(self.ui.actionAddUser.text())
        self.addUserDialog = AddUser()
        self.addUserDialog.show()
        
    def editItems(self, checked):
        print(self.ui.actionEditItems.text())
        self.editItemsDialog = EditItems()
        self.editItemsDialog.show()
        
    def statistics(self, checked):
        print(self.ui.actionStatistics.text())
        self.statisticsDialog.show()
        
    def editUsers(self, checked):
        print(self.ui.actionEditUsers.text())
        self.editUsersDialog = EditUsers()
        self.editUsersDialog.show()
        
    def loadUser(self, checked):
        print(self.ui.actionLoadUser.text())
        self.readCardDialog = ReadCard()
        self.readCardDialog.show()
        
    def about(self, checked):
        print(self.ui.actionAbout.text())
        _translate = QtCore.QCoreApplication.translate
        aboutBox = QMessageBox.about(self, _translate("aboutDialog", "Om"), _translate("aboutDialog", """<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li { white-space: pre-wrap; }\n
</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyQt NatCafé FVK-system v%1</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kontokortsystem til fredagsbaren på NAT, RUC</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright &copy; 2018 Marc John Bordier Dam, mjbd@ruc.dk</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright &copy; 2007 Toke Høiland-Jørgensen, toke@toke.dk</p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left
        :0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is free software: you can redistribute it and/or modify</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">it under the terms of the GNU General Public License as published </p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by the Free Software Foundation, either version 3 of the License, </p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or (at your option) any later version.</p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n
<p style=\" margin-top:0px; margin-botto
        m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is distributed in the hope that it will be useful,</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but WITHOUT ANY WARRANTY; without even the implied warranty of</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License for more details.</p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You should have received a copy of the GNU General Public License</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">along with this program.  If not, see <a href=\"http://www.gnu.org/licenses/\">http://www.gnu.org/licenses/</a>.</p></body></html>"""))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  gui = FVK()
  gui.show()
  sys.exit(app.exec_())
