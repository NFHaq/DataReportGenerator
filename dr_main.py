import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dataReportGen1 import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.onButton.clicked.connect(self.test)
        self._check_close = True

    def test(self):
        print('test')
        self._check_close = not self._check_close

    def closeEvent(self, event):
        if self._check_close:
            result = QtWidgets.QMessageBox.question(
                self, 'Confirm Close', 'Are you sure you want to close?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()