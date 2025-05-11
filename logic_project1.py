from PyQt6.QtWidgets import *
from gui_project1 import *

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


class VotingWindow(QMainWindow, Ui_input_voting_terminal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.check_submission)


    def check_submission(self):
        self.error_candidate_name_label.setText("")
        voterid_text = self.voterid_input.text().strip()
        candidate = 0

        if self.radio_can1.ischecked():
            candidate = 'Bianca'
        elif self.radio_can2.ischecked():
            candidate = 'Jack'
        elif self.radio_can3.ischecked():
            candidate = 'Nicole'
        elif self.radio_custom.ischecked:
            custom_candidate(self.custom_input)
        else:
            self.error_candidate_name_label.setText('error: select candidate')
            return

        try:
            if voterid_text < 9999 or voterid_text > 100000:
                print('error: enter valid voter ID')
                print('ex: 12345')
                return
            else:
                print(f'Voter {voterid_text} voted for {candidate}.')
        except:
            self.error_candidate_name_label.setText('error: enter valid input')



def custom_candidate():
    print('test')
