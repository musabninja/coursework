import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, 
    QStatusBar,QMenu
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    #Main Window
    def __init__(self, parent=None):
        #Initialiser
        super().__init__(parent)

        self.setWindowTitle("Image Editor by Mus'Ab Al-Bahry")
        self.resize(400, 200)
        self._createMenuBar()
    def _createMenuBar(self):
        class menuCreation():
            def __init__(self2,name):
                menuBar = self.menuBar()
                self.setMenuBar(menuBar)
                self2.name = name
                self2.menucreation = QMenu(self2.name,self)
                menuBar.addMenu(self2.menucreation)

        # Creating menus using my easy menu creation class
        file = menuCreation("File")
        effects = menuCreation("Effects")
        about = menuCreation("About")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())