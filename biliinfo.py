import json
import requests
from PyQt5 import uic
from PySide2.QtWidgets import QApplication
import reorganize

class main:

    def Repeater(self):
        input_uid = self.ui.lineEdit.text()  # 从输入框获得用户输入的文本信息，单行显示

        print("输入的uid：", input_uid)
        # global input_uid
        input_uid = int(input_uid)
        main.get_info(self, input_uid)

    def get_info(self, input_uid):
        data = requests.get('https://api.bilibili.com/x/web-interface/card?mid=%d' % (input_uid))

        reorganize.info(data)


    def show_info(self):
        value = self.lineEdit.text()
        self.lcdNumber.display(value)
        self.label.setText(value)



    def OpenB(self):
        self.BWindow = BWindow()
        self.BWindow.show()





    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("index.ui")
        # QString mString = ui->lineEdit->text();
        # QMessageBox::about(this, "About", mString);
        self.ui.button.clicked.connect(self.Repeater)


class info:
    def __init__(self):
        print("it is in info")


app = QApplication([])
stats = main()
stats.ui.show()
app.exec_()
