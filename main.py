#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys

from chmslGui import *
from chmslControl import *

activebtns = []
schedbtns = []
##stackedWidget = 0
##groupBox = 0
##statusBar = 0
##startAutoBtn = 0
autotestDelay = 1 # in seconds

class chmslBench(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.chmsl = chmslControl()
        
        global activeBtns, schedBtns

##        stackedWidget = self.stackedWidget
##        groupBox = self.groupBox
##        statusBar = self.statusbar
##        startAutoBtn = self.startAutoBtn
        
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

        activeBtns[0].clicked.connect(lambda: self.setActivePWM(0))
        activeBtns[1].clicked.connect(lambda: self.setActivePWM(1))
        activeBtns[2].clicked.connect(lambda: self.setActivePWM(2))
        activeBtns[3].clicked.connect(lambda: self.setActivePWM(3))
        activeBtns[4].clicked.connect(lambda: self.setActivePWM(4))
        activeBtns[5].clicked.connect(lambda: self.setActivePWM(5))
        activeBtns[6].clicked.connect(lambda: self.setActivePWM(6))
        activeBtns[7].clicked.connect(lambda: self.setActivePWM(7))
        activeBtns[8].clicked.connect(lambda: self.setActivePWM(8))
        activeBtns[9].clicked.connect(lambda: self.setActivePWM(9))
        activeBtns[10].clicked.connect(lambda: self.setActivePWM(10))
        activeBtns[11].clicked.connect(lambda: self.setActivePWM(11))
        activeBtns[12].clicked.connect(lambda: self.setActivePWM(12))
        activeBtns[13].clicked.connect(lambda: self.setActivePWM(13))
        activeBtns[14].clicked.connect(lambda: self.setActivePWM(14))

        schedBtns[0].clicked.connect(lambda: self.setSchedPWM(0))
        schedBtns[1].clicked.connect(lambda: self.setSchedPWM(1))
        schedBtns[2].clicked.connect(lambda: self.setSchedPWM(2))
        schedBtns[3].clicked.connect(lambda: self.setSchedPWM(3))
        schedBtns[4].clicked.connect(lambda: self.setSchedPWM(4))
        schedBtns[5].clicked.connect(lambda: self.setSchedPWM(5))
        schedBtns[6].clicked.connect(lambda: self.setSchedPWM(6))
        schedBtns[7].clicked.connect(lambda: self.setSchedPWM(7))
        schedBtns[8].clicked.connect(lambda: self.setSchedPWM(8))
        schedBtns[9].clicked.connect(lambda: self.setSchedPWM(9))
        schedBtns[10].clicked.connect(lambda: self.setSchedPWM(10))
        schedBtns[11].clicked.connect(lambda: self.setSchedPWM(11))
        schedBtns[12].clicked.connect(lambda: self.setSchedPWM(12))
        schedBtns[13].clicked.connect(lambda: self.setSchedPWM(13))

        self.activeBtn.clicked.connect(self.showActive)
        self.scheduleBtn.clicked.connect(self.showSchedule)

        self.startAutoBtn.clicked.connect(lambda: self.runAutoTest())

        self.statusbar.showMessage('Ready')

    def setActivePWM(self, idx):
        self.chmsl.setPWM(activePWM1[idx], activePWM2[idx])
        self.statusbar.showMessage('Active (Flashing), PWM1 DC: {}%, PWM2 DC: {}%'.format(activePWM1[idx], activePWM2[idx]))

    def setSchedPWM(self, idx):
        self.chmsl.setPWM(schedPWM1[idx], schedPWM2[idx])
        self.statusbar.showMessage('Schedule (Solid), PWM1 DC: {}%, PWM2 DC: {}%'.format(schedPWM1[idx], schedPWM2[idx]))


    def print_test(self):
        print('test')

    def showActive(self):
        self.stackedWidget.setCurrentIndex(0)
        self.groupBox.setTitle('Active Charging')

    def showSchedule(self):
        self.stackedWidget.setCurrentIndex(1)
        self.groupBox.setTitle('Schedule Charging')

    def disAllBtns(self):
        for eachBtn in activeBtns:
            eachBtn.setEnabled(False)
        for eachBtn in schedBtns:
            eachBtn.setEnabled(False)

    def enAllBtns(self):
        for eachBtn in activeBtns:
            eachBtn.setEnabled(True)
        for eachBtn in schedBtns:
            eachBtn.setEnabled(True)

    # run autotest in a separate thread
    def runAutoTest(self):
        global autoTestThreadExit
        print('Starting Auto Test.\n')
        autoTestThreadExit = False
        #self.disAllBtns()
        #self.autoTest()
        self.startAutoBtn.setText('Stop Auto Test')
        self.startAutoBtn.clicked.disconnect()
        self.startAutoBtn.clicked.connect(lambda: self.stopAutoTest())

        thread = threading.Thread(target=self.autoTest, args=())
        thread.daemon = True
        thread.start()
       
        
    # raise exit flag for autotest to stop
    def stopAutoTest(self):
        global autoTestThreadExit
        self.statusbar.showMessage('Auto test stopped')
        print('Stopping Auto Test.\n')
        autoTestThreadExit = True
        #self.enAllBtns()
        self.startAutoBtn.setText('Start Auto Test')
        self.startAutoBtn.clicked.disconnect()
        self.startAutoBtn.clicked.connect(lambda: self.runAutoTest())


    def autoTest(self):
        print('Auto test thread running...')
        global autoTestThreadExit
        self.statusbar.showMessage('Auto test started')
        self.showActive()

        for eachBtn in activeBtns:
            if autoTestThreadExit: return
            eachBtn.click()
            eachBtn.setDown(True)
            time.sleep(autotestDelay)
            eachBtn.setDown(False)

        self.showSchedule()
        time.sleep(1)

        for eachBtn in schedBtns:
            if autoTestThreadExit: return
            eachBtn.click()
            eachBtn.setDown(True)
            time.sleep(autotestDelay)
            eachBtn.setDown(False)

        self.stopAutoTest()
        self.update()
        


##    class autoTest(object):
##        global autoTestThreadExit
##        
##        def __init__(self):
##            thread = threading.Thread(target=self.run, args=())
##            thread.daemon = True                
##            thread.start()                                  
##
##        def run(self):
##            global autoTestThreadExit
##            statusBar.showMessage('Running auto test')
##            print('Auto test thread running...')
##            for eachBtn in activeBtns:
##                if autoTestThreadExit: return
##                eachBtn.click()
##                eachBtn.setDown(True)
##                time.sleep(autotestDelay)
##                eachBtn.setDown(False)
##
##            
##            stackedWidget.setCurrentIndex(1)
##            groupBox.setTitle('Schedule Charging')
##            time.sleep(0.2)
##
##            for eachBtn in schedBtns:
##                if autoTestThreadExit: return
##                eachBtn.click()
##                eachBtn.setDown(True)
##                time.sleep(autotestDelay)
##                eachBtn.setDown(False)
##
##            statusBar.showMessage('Auto test stopped')
##            startAutoBtn.setText('Start Auto Test')
##            startAutoBtn.clicked.disconnect()
##            startAutoBtn.clicked.connect(lambda: self.runAutoTest())
##
##            
##
##            stackedWidget.setCurrentIndex(0)
##            groupBox.setTitle('Active Charging')
##            
##            x = chmslControl()
##
##            # active charging testing
##            for dc1, dc2, b in zip(activePWM1, activePWM2, activeBtns):
##                if autoTestThreadExit:
##                    return                
##                x.setPWM(dc1=dc1, dc2=dc2)
##                #print('dc1: {}, dc2: {}'.format(dc1, dc2))
##                time.sleep(autotestDelay)
##
##            # schedule charging testing
##            for dc1, dc2 in zip(schedPWM1, schedPWM2):
##                if autoTestThreadExit:
##                    return                
##                x.setPWM(dc1=dc1, dc2=dc2)
##                #print('dc1: {}, dc2: {}'.format(dc1, dc2))
##                time.sleep(autotestDelay)
##
##            autoTestThreadExit = True
       
def main():
    app = QApplication(sys.argv)
    form = chmslBench()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
