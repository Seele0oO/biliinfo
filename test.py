# import ui_denglu as dl
# import ui_zhuche as zc

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = dl.Ui_submit_user()
        self.main_ui.setupUi(self)


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = zc.Ui_MainWindow()
        self.child.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()
    # 通过toolButton将两个窗体关联
    btn = window.main_ui.pushButton_new
    btn.clicked.connect(child.show)
    # 显示
    window.show()
    sys.exit(app.exec_())
# [点击并拖拽以移动]
# https: // blog.csdn.net / weixin_39449466 / article / details / 81008711  # 原地址链接