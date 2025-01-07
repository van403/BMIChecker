from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
# from result_win import ResultWin
from instr import *

class InputWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.name_label = QLabel(txt_name)
        self.name_input = QLineEdit()

        self.age_label = QLabel(txt_age)
        self.age.input = QLineEdit()

        self.height.label = QLabel(txt_height)
        self.height_input = QLineEdit()

        self.weight_label = QLabel(txt_weight)
        self.weight_input = QLineEdit()

        self.calculate_button = QPushButton(txt_calculate)
        self.calculate_button.clicked.connect(self.calculate)