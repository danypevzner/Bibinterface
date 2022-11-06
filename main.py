import sys
from PyQt5 import QtWidgets, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.id_edit = QtWidgets.QLineEdit(self)
        self.id_edit.textChanged.connect(self.text_changed)
        self.id_edit.setPlaceholderText('Введите ID')

        self.fio_edit = QtWidgets.QLineEdit(self)
        self.fio_edit.textChanged.connect(self.text_changed)
        self.fio_edit.setPlaceholderText('Введите ФИО')

        self.date_edit = QtWidgets.QLineEdit(self)
        self.date_edit.textChanged.connect(self.text_changed)
        self.date_edit.setPlaceholderText('Введите год')

        self.date_cbox = QtWidgets.QComboBox(self)
        self.date_cbox.currentIndexChanged.connect(self.boxclicked)
        self.date_cbox.addItems([">"])
        self.date_cbox.addItems(["<"])
        self.date_cbox.addItems(["="])

        self.name_edit = QtWidgets.QLineEdit(self)
        self.name_edit.textChanged.connect(self.text_changed)
        self.name_edit.setPlaceholderText('Введите название')

        self.strictbox = QtWidgets.QCheckBox(self)
        self.strictbox.clicked.connect(self.boxclicked)



      #  self.year_edit.textChanged.connect(self.text_changed)
      #  self.year_edit.setPlaceholderText('Введите год')

        self.btn = QtWidgets.QPushButton("Искать")
        self.btn.clicked.connect(self.btn_clicked)

        layout = QtWidgets.QFormLayout(self)

        layout.addRow('Введите ID', self.id_edit)
        layout.addRow('Введите ФИО', self.fio_edit)
        layout.addRow('Введите название', self.name_edit)
        layout.addRow('Строгое соответствие', self.strictbox)
        layout.addRow('Введите год',self.date_edit)
        layout.addRow('От/До/Cтрого', self.date_cbox)
        layout.addRow('Искать -->', self.btn)

    def text_changed(self, text):
        pass

    def boxclicked(self, text):
        pass

    def btn_clicked(self):
        print(f'{self.id_edit.text()} {self.name_edit.text()} {self.fio_edit.text()} {self.strictbox.isChecked()} {self.date_edit.text()} {self.date_cbox.currentIndex()}')  #


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())