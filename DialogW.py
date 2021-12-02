from MainW import MainWindow
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class DialogWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        self.label = QLabel()
        self.label.setText('Enter your instagram login ang password')

        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(lambda: self.the_button_was_clicked())

        layout = QVBoxLayout()
        widgets = [
            self.label,
            self.login,
            self.password,
            self.button
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        login = self.login.text()
        password = self.password.text()
        print(login)
        print(password)

        window1 = MainWindow(self)
        window1.show()
        self.close()







