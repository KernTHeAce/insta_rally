from userInterface import DialogWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
import sys



app = QApplication(sys.argv)

window = DialogWindow()
window.show()
app.exec()