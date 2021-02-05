import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget,QLineEdit

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")
        self.button1=QPushButton("退出应用程序")
        self.Line1=QLineEdit()
        self.x=self.Lin
        self.button1.clicked.connect(self.onClick_Button)
        layout=QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.Line1)
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    #按钮单机事件的方法
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+"按钮被按下")
        print(self.x)
        app=QApplication.instance()
        app.quit()


#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())