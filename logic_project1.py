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
        custom_candidate = 0

        try:

            voterid_text = int(voterid_text)
            if voterid_text < 10000 or voterid_text > 99999:
                self.error_candidate_name_label.setText("Error: Voter ID must be 5 digits.")
                return

        except ValueError:

            self.error_candidate_name_label.setText("Error: Voter ID must be a number.")
            return

        if self.radio_can1.isChecked():
            candidate = 'Bianca'
        elif self.radio_can2.isChecked():
            candidate = 'Jack'
        elif self.radio_can3.isChecked():
            candidate = 'Nicole'
        elif self.radio_custom.isChecked():
            custom_candidate = validate_custom_candidate(self.custom_input.text())
        else:
            self.error_candidate_name_label.setText('error: select candidate')
            return

        if custom_candidate == 0:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {candidate}')
        else:
            self.error_candidate_name_label.setText(f'Voter (ID:{voterid_text}) voted for {custom_candidate}')


def validate_custom_candidate(name: str):
    name = name.strip()
    if not name:
        return 0
    else:
        return name


