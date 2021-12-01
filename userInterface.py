import datetime
import sys
from datetime import date, time

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QGridLayout,
    QGroupBox
)


# Subclass QMainWindow to customize your application's main window
class DialogWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        self.label = QLabel()
        self.label.setText('Enter your instagram login ang password')

        self.login = QLineEdit()
        self.login.setMaxLength(50)
        self.login.setPlaceholderText("Login")

        self.password = QLineEdit()
        self.password.setMaxLength(50)
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        label1 = QLabel()
        label2 = QLabel()
        label1.setText('Enter link to the post')
        label2.setText('Choose')

        self.link = QLineEdit()
        # self.link.setMaxLength(250)
        self.link.setPlaceholderText("Link")

        subscribe_on_me = QRadioButton()
        subscribe_on_me.setText('Subscribe on me')

        liker = QRadioButton()
        liker.setText('Liker')

        repost = QRadioButton()
        repost.setText('Repost')

        sponsors = QLineEdit()
        sponsors.setPlaceholderText('Enter sponsors accounts')

        final = QDateTimeEdit()
        final.setDate(date.today())
        final.setTime(datetime.datetime.now().time())

        winners = QListWidget()
        # winners.insertItem(0, '0')
        # winners.clicked.connect(lambda: self.item_clicked())

        button = QPushButton("Random")
        button.clicked.connect(lambda: self.the_button_was_clicked())

        layout = QGridLayout()
        groupbox = QGroupBox("GroupBox Example")
        layout.addWidget(groupbox)
        widgets = [
            label1,
            self.link,
            label2,
            subscribe_on_me,
            liker,
            repost,
            sponsors,
            final,
            button
        ]
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        for index, item in enumerate(widgets):
            vbox.addWidget(item)

        layout.addWidget(groupbox, 0, 0)
        layout.addWidget(winners, 0, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        pass


