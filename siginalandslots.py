from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import QRect,QSize
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = " PyQt5 events and siginals"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "icon.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        
        self.CreateButton()
        self.show()

    def CreateButton(self):
        button = QPushButton("Close", self)
        # buttom.move(50, 50)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon("icon.png"))
        button.setIconSize(QSize(40, 40))
        button.setToolTip("<h3>This is click me button<h3> ")
        button.clicked.connect(self.ClickMe) 

    def ClickMe(self):
        sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec())

