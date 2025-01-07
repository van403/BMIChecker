from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from instr import*

class ResultWin(QWidget):
    def __init__(self, bmi):
        super().__init__()
        self.bmi = bmi
        self.initUI()
        self.set_apppear()
        self.show()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.result_label = QLabel(txt_result +f" {self.bmi:.2f}")

        if self.bmi < 18.5:
            self.category_label = QLabel(txt_underweight)
        elif 18.5 <= self.bmi < 25:
            self.category_label = QLabel(txt_normal)
        elif 25 <= self.bmi < 30:
            self.category_label = QLabel(txt_overweight)
        else:
            self.category_label = QLabel(txt_obesity)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(8)

        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.exit_button)
        self.setLayout(self.layout)

    def set_appear(self):
        self.setWindowTitle("BMI Checker - Result")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)