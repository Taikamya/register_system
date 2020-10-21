from application import *


def main():
    app = QApplication(sys.argv)
    if (QDialog.Accepted == True):
        window = MainWindow()
        window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
