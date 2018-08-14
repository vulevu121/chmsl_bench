#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys

from chmslGui import *
from chmslControl import *


class chmslBench(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.chmsl = chmslControl()
        

        activeBtns = [self.pushButton_1,
                      self.pushButton_2,
                      self.pushButton_3,
                      self.pushButton_4,
                      self.pushButton_5,
                      self.pushButton_6,
                      self.pushButton_7,
                      self.pushButton_8,
                      self.pushButton_9,
                      self.pushButton_10,
                      self.pushButton_11,
                      self.pushButton_12,
                      self.pushButton_13,
                      self.pushButton_14,
                      self.pushButton_15]

        schedBtns = [self.pushButton_46,
                     self.pushButton_47,
                     self.pushButton_48,
                     self.pushButton_49,
                     self.pushButton_50,
                     self.pushButton_51,
                     self.pushButton_52,
                     self.pushButton_53,
                     self.pushButton_54,
                     self.pushButton_55,
                     self.pushButton_56,
                     self.pushButton_57,
                     self.pushButton_58,
                     self.pushButton_59]
        
        activeBtns[0].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[0], activePWM2[0]))
        activeBtns[1].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[1], activePWM2[1]))
        activeBtns[2].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[2], activePWM2[2]))
        activeBtns[3].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[3], activePWM2[3]))
        activeBtns[4].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[4], activePWM2[4]))
        activeBtns[5].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[5], activePWM2[5]))
        activeBtns[6].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[6], activePWM2[6]))
        activeBtns[7].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[7], activePWM2[7]))
        activeBtns[8].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[8], activePWM2[8]))
        activeBtns[9].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[9], activePWM2[9]))
        activeBtns[10].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[10], activePWM2[10]))
        activeBtns[11].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[11], activePWM2[11]))
        activeBtns[12].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[12], activePWM2[12]))
        activeBtns[13].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[13], activePWM2[13]))
        activeBtns[14].clicked.connect(lambda: self.chmsl.setPWM(activePWM1[14], activePWM2[14]))

        schedBtns[0].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[0], schedPWM2[0]))
        schedBtns[1].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[1], schedPWM2[1]))
        schedBtns[2].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[2], schedPWM2[2]))
        schedBtns[3].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[3], schedPWM2[3]))
        schedBtns[4].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[4], schedPWM2[4]))
        schedBtns[5].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[5], schedPWM2[5]))
        schedBtns[6].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[6], schedPWM2[6]))
        schedBtns[7].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[7], schedPWM2[7]))
        schedBtns[8].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[8], schedPWM2[8]))
        schedBtns[9].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[9], schedPWM2[9]))
        schedBtns[10].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[10], schedPWM2[10]))
        schedBtns[11].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[11], schedPWM2[11]))
        schedBtns[12].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[12], schedPWM2[12]))
        schedBtns[13].clicked.connect(lambda: self.chmsl.setPWM(schedPWM1[13], schedPWM2[13]))


        self.activeBtn.clicked.connect(self.showActive)
        self.scheduleBtn.clicked.connect(self.showSchedule)

    def print_test(self):
        print('test')

    def showActive(self):
        self.stackedWidget.setCurrentIndex(0)
        self.groupBox.setTitle('Active Charging')

    def showSchedule(self):
        self.stackedWidget.setCurrentIndex(1)
        self.groupBox.setTitle('Schedule Charging')
       
def main():
    app = QApplication(sys.argv)
    form = chmslBench()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
