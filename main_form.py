# this code is a part of the main_form_ui to enter data
# mysql table for users :
# create table users (nameid int not null auto_increment, 
# name varchar(50),
# email varchar(50),
# telefone varchar(20),
# primary key(nameid));

from PyQt5 import uic,QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "me",
    database = "store"
)



def main_function():
    cursor = db.cursor()
    command = "select * from users"
    cursor.execute(command)
 
    result = cursor.fetchall()
    self.tableWidget.setRowCount(0)
    for row_number, row_data in enumerate(result):
        print(row_number)
        self.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            #print(column_number)
            self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
 
 
    line1 = main_form.lineEdit.text()
    line2 = main_form.lineEdit_2.text()
    line3 = main_form.lineEdit_3.text()
    
    cursor = db.cursor()
    command = "insert into users (name, email, telefone) values (%s, %s, %s)"
    data = (line1, line2, line3)
    cursor.execute(command, data)
    db.commit()

app = QtWidgets.QApplication([])
main_form = uic.loadUi("main_form.ui")
main_form.buttonBox.clicked.connect(main_function)
main_form.show()
app.exec()
#cur = connection.cursor()
