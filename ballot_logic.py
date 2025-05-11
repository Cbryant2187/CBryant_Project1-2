from PyQt6.QtWidgets import *
from gui_project1 import *

class VotingWindow(QMainWindow, Ui_input_voting_terminal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.submit_vote)