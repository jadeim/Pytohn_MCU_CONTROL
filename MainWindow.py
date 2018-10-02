import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "MCU control Application"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 768

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("resources\Icons\Icon_image.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

def run():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    run()