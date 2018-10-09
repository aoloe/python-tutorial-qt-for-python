from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import QFile, Slot
from PySide2.QtUiTools import QUiLoader

class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)

    @Slot()
    def alert(self):
        alert = QMessageBox()
        alert.setText(self.text_field.text())
        alert.exec_()

    @Slot()
    def quit(self):
        quit()
        

if __name__ == '__main__':
    app = QApplication([])

    loader = QUiLoader()
    loader.registerCustomWidget(Dialog)

    dialog = loader.load('alert-quit.ui')
    dialog.show()

    app.exec_()
