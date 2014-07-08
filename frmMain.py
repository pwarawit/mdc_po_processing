# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created: Tue Jul 08 10:43:30 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmMain(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(609, 395)
        self.verticalLayoutWidget = QtGui.QWidget(frmMain)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 581, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblMessage = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.verticalLayout.addWidget(self.lblMessage)
        self.txtMessage = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.txtMessage.setObjectName(_fromUtf8("txtMessage"))
        self.verticalLayout.addWidget(self.txtMessage)
        self.horizontalLayoutWidget = QtGui.QWidget(frmMain)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblFolder = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lblFolder.setObjectName(_fromUtf8("lblFolder"))
        self.horizontalLayout.addWidget(self.lblFolder)
        self.txtFolder = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.txtFolder.setText(_fromUtf8(""))
        self.txtFolder.setObjectName(_fromUtf8("txtFolder"))
        self.horizontalLayout.addWidget(self.txtFolder)
        self.btnProcess = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnProcess.setObjectName(_fromUtf8("btnProcess"))
        self.horizontalLayout.addWidget(self.btnProcess)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "PO Processing", None))
        self.lblMessage.setText(_translate("frmMain", "Message:", None))
        self.lblFolder.setText(_translate("frmMain", "Folder: ", None))
        self.btnProcess.setText(_translate("frmMain", "Process", None))
	self.btnProcess.clicked.connect(self.process)

    def process(self):
        print "TEST"
        self.txtMessage.setText("This is an empty field")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ex = Ui_frmMain()
	ex.show()
	sys.exit(app.exec_())


