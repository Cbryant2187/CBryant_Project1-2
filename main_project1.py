from gui_project1 import *
from logic_project1 import logic

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = logic()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()