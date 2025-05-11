from logic_project1 import *
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Logic()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()