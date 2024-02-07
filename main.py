
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget # 전자는 애플리케이션 핸들러, 후자는 빈 GUI 위젯

class Calculator(QWidget):

    def __init__(self) :
        super().__init__() # QWidget껄 상속받겠다.
        self.initUI() # 나머지는 initUI()에서 정의하겠다.

    def initUI(self):
        self.setWindowTitle('Calculator') # 윈도우에 표시되는 타이틀 이름을 칼큘레이터로 하겠다.
        self.resize(256, 256) # 크기
        self.show()

if __name__ == '__main__' : # pyqt는 앱당 1개의 QApplication이 필요.
    app = QApplication(sys.argv) # 인스턴스 생성
    view = Calculator() # 윈도 인스턴스 생성
    sys.exit(app.exec_()) # 애플리케이션이 이벤트 처리를 하도록 루프 구동

