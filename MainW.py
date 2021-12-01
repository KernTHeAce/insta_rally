import datetime
from datetime import date
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QDateTimeEdit,
    QGridLayout,
    QListWidget,
    QGroupBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label1.setText('Enter link to the post')
        self.label2.setText('Choose')

        self.link = QLineEdit()
        self.link.setPlaceholderText("Link")

        self.subscribe_on_me = QRadioButton()
        self.subscribe_on_me.setText('Subscribe on me')

        self.liker = QRadioButton()
        self.liker.setText('Liker')

        self.repost = QRadioButton()
        self.repost.setText('Repost')

        self.sponsors = QLineEdit()
        self.sponsors.setPlaceholderText('Enter sponsors accounts')

        self.final = QDateTimeEdit()
        self.final.setDate(date.today())
        self.final.setTime(datetime.datetime.now().time())

        self.winners = QListWidget()

        self.button = QPushButton("Random")
        self.button.clicked.connect(lambda: self.the_button_was_clicked())

        layout = QGridLayout()
        self.groupbox = QGroupBox("GroupBox Example")
        layout.addWidget(self.groupbox)
        widgets = [
            self.label1,
            self.link,
            self.label2,
            self.subscribe_on_me,
            self.liker,
            self.repost,
            self.sponsors,
            self.final,
            self.button
        ]
        vbox = QVBoxLayout()
        self.groupbox.setLayout(vbox)
        for index, item in enumerate(widgets):
            vbox.addWidget(item)

        layout.addWidget(self.groupbox, 0, 0)
        layout.addWidget(self.winners, 0, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        pass

    def fill_list_box(self, name_list):
        for index, item in enumerate(name_list):
            self.winners.insertItem(index + 1, item)


