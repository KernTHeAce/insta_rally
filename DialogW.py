from MainW import MainWindow
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
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

        button = QPushButton("Press Me!")
        button.clicked.connect(lambda: self.the_button_was_clicked())

        layout = QVBoxLayout()
        widgets = [
            self.label,
            self.login,
            self.password,
            button
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

        window1 = MainWindow()
        window1.show()

        self.close()


