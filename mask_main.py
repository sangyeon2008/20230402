from mask_api import *  # api 불러오는 함수
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5 import uic
form_class = uic.loadUiType("mask_ui.ui")[0]   # 내가 만든 UI파일 불러오기

class WindowClass(QMainWindow,form_class):
    def __init__(self):
        # 창 초기화
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Today Mask")
        self.setWindowIcon(QIcon('mask_4.png'))
        self.btn_show_mask.clicked.connect(self.get_image)
        self.pm10, self.pm25,self.O3 = get_masknum()            # self.항목3 추가
        print(self.pm10, self.pm25, self.O3)
        self.mask_label.setText("push show mask")
        self.O3_label.setText("오존 수치:  ")
        self.pm10_label.setText(f"미세먼지 농도:")
        self.pm25_label.setText(f"초 미세먼지 농도: ")
        # self.항목3의 초기 텍스트값 설정

    def get_image(self):
        # 미세먼지와 초미세먼지 평균치를 가지고 와서 이미지 순번을 만듬
        # avg = self.get_avg(self.pm10, self.pm25,self.O3)    # 평균치를 구하는 함수 get_avg에 항목3도 추가해서 평균치 가져오기
        avg = 3
        # QPixmap 클래스를 통해 qPixmapVar 객체를 만들고 load메서드로 이미지를 불러옴
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load(f"mask_{avg}.png")
        # 가져온 이미지의 크기가 각기 다를수 있으므로 사이즈 조절
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(250)
        # 미리 만들어 둔 mask_label에 이미지 적용
        self.mask_label.setPixmap(self.qPixmapVar)
        # 미세먼지 초미세먼지 수치 표시
        self.pm10_label.setText(f"미세먼지 농도: {self.pm10}")
        self.pm25_label.setText(f"초 미세먼지 농도: {self.pm25}")
        # self.항목3의 수치 표시
        self.O3_label.setText(f"오존 수치: {self.O3}")
    def get_avg(self, pm10, pm25):
        # pm10(미세먼지) 수치별 기준: 0 ~ 80: 좋음, 80~150: 약간 나쁨,  150~ 300: 주의보(나쁨), 300~: 경보(매우 나쁨)
        p10, p25 = 4, 4
        pm10_std = [80, 150, 300]
        # pm25(초미세먼지) 수치별 기준:0~ 40: 좋음, 40~ 75: 약간 나쁨,  75~150: 주의보(나쁨),  150~ 경보(매우나쁨)
        pm25_std = [40, 75, 150]
        for i in range(3):
            if pm10 < pm10_std[i]:
                p10 = i + 1
                break
        for i in range(3):
            if pm25 < pm25_std[i]:
                p25 = i + 1
                break
        return (p10 + p25) // 2

if __name__ == "__main__":
    # sys.argv: 현재 경로 -> 실행
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    # 실행만 하면 코드를 다 읽는 순간 종료되기 때문에
    # 실행창을 유지하는 행위
    app.exec_()