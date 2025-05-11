from ballot_logic import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exit_option_button.clicked.connect(self.close_window)
        self.vote_option_button.clicked.connect(self.open_voting_window)

    def close_window(self):
        self.close()

    def open_voting_window(self):
        self.voting_window = VotingWindow()
        self.voting_window.show()
        self.hide()





