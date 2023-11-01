import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from PyQt5 import uic # Qt Desiner 에서 만든 UI를 연결시켜주는 라이브러리

from_class = uic.loadUiType("ui/mainUi.ui")[0]
# Qt Desiner에서 만든 ui를 불러옴

class MyWin(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 제작해 놓은 ui를 불러오기

        self.setWindowTitle("연습 프로그램") # 윈도우 타이틀
        self.setWindowIcon(QIcon("img/google.png")) #윈도우 아이콘
        self.statusBar().showMessage("Test Program v0.5 2023-11-01")

        self.btn1.clicked.connect(self.btn1_clicked) # 버튼1이 클릭되면 메서드 btn1_clicked 호출
        self.btn2.clicked.connect(self.btn2_clicked) # 버튼2이 클릭되면 메서드 btn2_clicked 호출
        self.btn3.clicked.connect(self.btn3_clicked) # 버튼3이 클릭되면 메서드 btn3_clicked 호출
        self.btn4.clicked.connect(self.btn4_clicked) # 버튼4이 클릭되면 메서드 btn4_clicked 호출
        self.init_btn.clicked.connect(self.init)  # RESET이 클릭되면 메서드 init 호출

        self.lineEdit.textChanged.connect(self.changePrint)
        # lineEdit에 텍스트가 변경될 때마다 changePrint 함수가 실행

        self.lineEdit.returnPressed.connect(self.changePrint)
        # lineEdit에 텍스트가 입력 중(lineEdit가 선택 중)에 엔터키가 클릭되면 changePrint 함수가 실행됨

    def btn1_clicked(self): # 버튼1이 클릭되었을떄 실행될 메서드
        # print("버튼1번이 클릭되었습니다!!!")
        self.lineEdit.setText("버튼1번이 클릭되었습니다")
        # lineEdit에 setText() 가로 안의 문자열이 출력됨

    def btn2_clicked(self): # 버튼2이 클릭되었을떄 실행될 메서드
        # print("버튼2번이 클릭되었습니다!!!")
        self.textEdit.append("버튼2번이 클릭되었습니다")

    def btn3_clicked(self):
        user_text = self.lineEdit.text() # 사용자가 입력한 텍스트 가져오기
        print(user_text)

    def btn4_clicked(self):
        user_intro = self.textEdit.toPlainText() # 사용자가 textEdit 입력한 텍스트 가져오기
        print(user_intro)

    def changePrint(self):
        user_text = self.lineEdit.text()
        print(user_text)

    def init(self):
        self.textEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    ex.show()
    sys.exit(app.exec_())

