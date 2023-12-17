# this code is a part of the main_form_ui to enter data
# mysql table for users :
# create table users (nameid int not null auto_increment, 
# name varchar(50),
# email varchar(50),
# telefone varchar(20),
# primary key(nameid));

from PyQt5 import uic,QtWidgets

def main_function():
    line1 = main_form.lineEdit.text()
    line2 = main_form.lineEdit_2.text()
    line3 = main_form.lineEdit_3.text()
    print (line1)
    print (line2)
    print (line3)

app = QtWidgets.QApplication([])
main_form = uic.loadUi("main_form.ui")
main_form.buttonBox.clicked.connect(main_function)

main_form.show()
app.exec()
