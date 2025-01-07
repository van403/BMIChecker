import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from input_win import InputWin
from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.welcome_text = QLabel(txt_welcome)
        self.start_button = QPushButton(txt_start)
        self.start_button.clicked.connect(self.next_window)

        self.layout.setCongratsMargins(10, 10, 10)
        self.layout.setSpacing(10)

        self.layout.addWidget(self.welcome_text)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

    def set_appear(self):
        self.setWindowTitle("BMI Checker")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def next_window(self):
        self.input_window = InputWin()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWin()
    sys.exit(app.exec_())
        