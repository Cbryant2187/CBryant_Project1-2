from test_gui import *

def main():
    application = QApplication([])
    window = QMainWindow()
    window.setGeometry(0, 0, 300, 100)
    window.show()
    application.exec()


if __name__ == '__main__':
    main()