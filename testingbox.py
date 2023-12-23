import sys
import PySide2
from PySide2 import QtWidgets, QtCore


class UserInput(object):
    def setupUi(self, get_user_input=None):
        # Basic shape
        self.width = 425
        get_user_input.setObjectName("get_user_input")
        get_user_input.resize(425, self.width)
        self.frame = QtWidgets.QFrame(get_user_input)
        self.frame.setGeometry(QtCore.QRect(11, 10, 401, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        # Creating the grid layout for most of the display elements
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.get_user_input_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.get_user_input_layout.setContentsMargins(5, 5, 5, 5)
        self.get_user_input_layout.setObjectName("get_user_input_layout")
        # Grid layout for the buttons
        self.buttonLayoutGrid = QtWidgets.QWidget(get_user_input)
        self.buttonLayoutGrid.setGeometry(QtCore.QRect(10, 390, 401, 41))
        self.buttonLayoutGrid.setObjectName("buttonLayoutGrid")
        self.buttonLayout = QtWidgets.QGridLayout(self.buttonLayoutGrid)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        # Buttons
        self.buttonOK = QtWidgets.QPushButton(self.buttonLayoutGrid)
        self.buttonOK.setObjectName("buttonOK")
        self.buttonOK.setText("OK")
        self.buttonLayout.addWidget(self.buttonOK, 0, 1, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton(self.buttonLayoutGrid)
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonCancel.setText("CANCEL")
        self.buttonLayout.addWidget(self.buttonCancel, 0, 2, 1, 1)

        #Column View Data
        self.t = PySide2.QtWidgets.QColumnView()
        self.t.setColumnWidths([10,10])

        model = PySide2.QtGui.QStandardItemModel()
        model.setColumnCount(1)
        model.setHorizontalHeaderLabels(['Data Collections'])

        self._dict = {'Test 1': [1, 2, 3], 'Test 2': [4, 5, 6], 'Test 3': [7, 8, 9]}
        _data = []

        for each in self._dict:
            resultItem = PySide2.QtGui.QStandardItem()
            insertText = each
            resultItem.setText(str(insertText))
            model.appendRow(resultItem)

        self.t.setModel(model)
        self.t.clicked.connect(self.column_view_clicked)
        self.get_user_input_layout.addWidget(self.t, 2,0,1,1)

    def column_view_clicked(self, row):
        model = PySide2.QtGui.QStandardItemModel()
        model.setColumnCount(1)
        model.setHorizontalHeaderLabels(['Analysis Variables'])
        _data = []

        for i in self._dict[row.data()]:
            resultItem = PySide2.QtGui.QStandardItem()
            resultItem.setText(str(i))
            model.appendRow(resultItem)

        self.t.createColumn(row)        

class UserInputPrompt(PySide2.QtWidgets.QDialog, UserInput):

    def __init__(self, path_to_image=None):
        app = PySide2.QtWidgets.QApplication(sys.argv)
        super(UserInputPrompt, self).__init__()
        self.setupUi(self)
        super(UserInputPrompt, self).exec_()        

    def get_user_input(self):
        print("Get user selection")