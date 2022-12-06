''' __  ___              __     _  ___        _     
   /  |/  /_ _____ ___ _/ /    / |/ (_)__    (_)__ _
  / /|_/ / // (_-</ _ `/ _ \  /    / / _ \  / / _ `/
 /_/  /_/\_,_/___/\_,_/_.__/ /_/|_/_/_//_/_/ /\_,_/ 
                                        |___/       
www.github.com/musabninja
'''

import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,QMenu,QLabel
)

# Window GUI Class
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Image Editor")
        self.resize(1050, 650)
        self._createMenuBar()
        # self.initUI()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)
        def createMenu(name):
            menuObj = QMenu(name,self)
            menuBar.addMenu(menuObj)
        file = createMenu("File")
        effects = createMenu("Effects")
        about = createMenu("About")

# Starting application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())