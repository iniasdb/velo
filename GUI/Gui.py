import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class PyCalcUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Velo station")
        self.setFixedSize(500, 250)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _create_buttons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'FIETS ONTLENEN': (0, 0),
                   'FIETS TERUGBRENGEN': (0, 1)
                }

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(200, 50)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def clear_display(self):
        self.setDisplayText('')
