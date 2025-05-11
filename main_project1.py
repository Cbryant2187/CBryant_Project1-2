from gui_project1 import *
from logic_project1 import *

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Logic()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()