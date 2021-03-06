# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exampleLoaderTemplate.ui'
#
# Created: Sat Feb 28 10:28:50 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 552)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.exampleTree = QtWidgets.QTreeWidget(self.widget)
        self.exampleTree.setObjectName("exampleTree")
        self.exampleTree.headerItem().setText(0, "1")
        self.exampleTree.header().setVisible(False)
        self.gridLayout.addWidget(self.exampleTree, 0, 0, 1, 2)
        self.graphicsSystemCombo = QtWidgets.QComboBox(self.widget)
        self.graphicsSystemCombo.setObjectName("graphicsSystemCombo")
        self.graphicsSystemCombo.addItem("")
        self.graphicsSystemCombo.addItem("")
        self.graphicsSystemCombo.addItem("")
        self.graphicsSystemCombo.addItem("")
        self.gridLayout.addWidget(self.graphicsSystemCombo, 2, 1, 1, 1)
        self.qtLibCombo = QtWidgets.QComboBox(self.widget)
        self.qtLibCombo.setObjectName("qtLibCombo")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.qtLibCombo.addItem("")
        self.gridLayout.addWidget(self.qtLibCombo, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.loadBtn = QtWidgets.QPushButton(self.widget)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 3, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadedFileLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loadedFileLabel.setFont(font)
        self.loadedFileLabel.setText("")
        self.loadedFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadedFileLabel.setObjectName("loadedFileLabel")
        self.verticalLayout.addWidget(self.loadedFileLabel)
        self.codeView = QtWidgets.QPlainTextEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        self.codeView.setFont(font)
        self.codeView.setObjectName("codeView")
        self.verticalLayout.addWidget(self.codeView)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.graphicsSystemCombo.setItemText(0, _translate("Form", "default"))
        self.graphicsSystemCombo.setItemText(1, _translate("Form", "native"))
        self.graphicsSystemCombo.setItemText(2, _translate("Form", "raster"))
        self.graphicsSystemCombo.setItemText(3, _translate("Form", "opengl"))
        self.qtLibCombo.setItemText(0, _translate("Form", "default"))
        self.qtLibCombo.setItemText(1, _translate("Form", "PyQt4"))
        self.qtLibCombo.setItemText(2, _translate("Form", "PySide"))
        self.qtLibCombo.setItemText(3, _translate("Form", "PyQt5"))
        self.label_2.setText(_translate("Form", "Graphics System:"))
        self.label.setText(_translate("Form", "Qt Library:"))
        self.loadBtn.setText(_translate("Form", "Run Example"))

