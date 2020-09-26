from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "wifiqr-gui"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
    
        self.show()
        

    def CreateLayout(self):
        self.groupBox = QGroupBox("Select!")
        gridLayout = QGridLayout()

        self.button = QPushButton("Create QR", self)
        # self.button.setIcon(QtGui.QIcon("icon.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        gridLayout.addWidget(self.button, 0,0)

        self.button1 = QPushButton("Generate QR", self)
        # self.button1.setIcon(QtGui.QIcon("icon.png"))
        self.button1.setIconSize(QtCore.QSize(40, 40))
        self.button1.setMinimumHeight(40)
        gridLayout.addWidget(self.button1, 1,0)

        self.button2 = QPushButton("Scan QR", self)
        # self.button2.setIcon(QtGui.QIcon("icon.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2, 2,0)

        self.groupBox.setLayout(gridLayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


