#from DialogW import DialogWindow
from datetime import datetime, date
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QCheckBox,
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
    QGroupBox,
    QTextEdit,
    QToolBar
)


class MainWindow(QMainWindow):
    def __init__(self, dialog):
        super().__init__()
        self.dialog = dialog

        self.setWindowTitle("Main Window")

        sing_in_button = QAction("&SingIn", self)
        help_button = QAction("&Help", self)
        sing_in_button.triggered.connect(self.sing_in_button)
        help_button.triggered.connect(self.help_button)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(sing_in_button)
        file_menu.addAction(help_button)

        self.WARNING_label = QLabel()
        self.WARNING_label.setText('')
        self.link_label = QLabel()
        self.link_label.setText('Enter link to the post')
        self.choose_label = QLabel()
        self.choose_label.setText('Choose')

        self.link = QLineEdit()
        self.link.setPlaceholderText("Link")

        self.following = QCheckBox()
        self.following.setText('Subscribe on me')

        self.liker = QCheckBox()
        self.liker.setText('Liker')

        self.repost = QCheckBox()
        self.repost.setText('Repost')

        self.sponsors = QTextEdit()
        self.sponsors.setPlaceholderText('Enter sponsors accounts')

        self.final = QDateTimeEdit()
        self.final.setDate(date.today())
        self.final.setTime(datetime.now().time())

        self.winners = QListWidget()

        self.button = QPushButton("Random")
        self.button.clicked.connect(lambda: self.the_button_was_clicked())

        layout = QGridLayout()
        self.groupbox = QGroupBox("GroupBox Example")
        layout.addWidget(self.groupbox)
        widgets = [
            self.WARNING_label,
            self.link_label,
            self.link,
            self.choose_label,
            self.following,
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

    def sing_in_button(self):
        self.close()
        self.dialog.show()

    def help_button(self):
        pass

    def check_parameters(self, parameters):
        self.WARNING_label.setStyleSheet('color: red')
        like = parameters['likes']
        following = parameters['following']
        repost = parameters['repost']

        if not parameters['link']:
            self.WARNING_label.setText('\tENTER LINK TO POST')
            return False
        elif not (like or following or repost):
            self.WARNING_label.setText('\tCHOOSE SOMETHING')
            return False
        else:
            self.WARNING_label.setStyleSheet('color: black')
            self.WARNING_label.setText('\tWait please)')
            return True

    def the_button_was_clicked(self):
        parameters = {
            'link': self.link.text(),
            'following': self.following.isChecked(),
            'likes': self.liker.isChecked(),
            'repost': self.repost.isChecked(),
            'sponsors': self.sponsors.toPlainText(),
            'time': self.final.dateTime().toPyDateTime()
        }

        if self.check_parameters(parameters):
            pass

    def fill_list_box(self, name_list):
        for index, item in enumerate(name_list):
            self.winners.insertItem(index + 1, item)


