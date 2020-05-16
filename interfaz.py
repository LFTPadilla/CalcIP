import os
import time
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from base_calculator import validator, convert_number_system
from ipaddress import dirHost, dirNetwork
sys.path.append(".")

# qtCreatorFile = "compilador/interfaz/interfazQT.ui" # Nombre del archivo aquí.
qtCreatorFile = "interfazQT.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnConvert.clicked.connect(self.ConvertBases)
        self.btnCalcHost.clicked.connect(self.ConvertipHost)
        self.btnCalcRed.clicked.connect(self.ConvertipRed)
        self.comboEnd.setCurrentIndex(1)

    def ConvertipHost(self):
        ip = self.ipHost.text()
        data = dirHost(ip)
        self.hDirRed.setText(data[0])
        self.hDirBroad.setText(data[1])
        self.hCant.setText(str(data[2]))
        self.hRange.setText(data[3]+"   -   "+data[3])
        print(data)

    def ConvertipRed(self):
        ip = self.ipRed.text()
        data = dirNetwork(ip)
        self.rMasc.setText(str(data[0]))
        self.rBroad.setText(str(data[1]))
        self.rCantRed.setText(str(data[2]))
        self.rCantHosts.setText(str(data[3]))
        self.rCantHostsAsing.setText(str(data[4]))
        self.rDirRed.setText(str(data[5][0]))
        self.rRange.setText(str(data[5]))

        print(dirNetwork(ip))

    def ConvertBases(self):
        user_number = self.numConvert.text()
        comboStart = self.comboStart.currentIndex()
        comboEnd = self.comboEnd.currentIndex()
        start = None
        end = None
        if(comboStart == 0):
            start = 10
        if(comboStart == 1):
            start = 2
        if(comboStart == 2):
            start = 16
        if(comboStart == 3):
            start = 8
        if(comboEnd == 0):
            end = 10
        if(comboEnd == 1):
            end = 2
        if(comboEnd == 2):
            end = 16
        if(comboEnd == 3):
            end = 8

        valid_input = validator(str(user_number), str(start), str(end))
        if(valid_input == False):
            print("VALOR INVALIDO")
            self.resultConvert.setText("Valor invalido")
            return
        print(str(user_number), str(start), str(end))
        self.resultConvert.setText(convert_number_system(
            str(user_number), str(start), str(end)))

    def limpiar(self):
        pass
        # self.listViewTokens.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
