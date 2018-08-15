from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from chmslGui import *
from chmslControl import *

activebtns = []
schedubtns = []

autotestDelay = 2 # in seconds
autotestThreadExit = False

class chmslBench(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.chmsl = chmslControl()
        
        global activeBtns, scheduBtns

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

        scheduBtns = [self.pushButton_46,
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

        for eachBtn, eachText in zip(activeBtns, activeBtnsText):
            eachBtn.setText(eachText)

        for eachBtn, eachText in zip(scheduBtns, scheduBtnsText):
            eachBtn.setText(eachText)

        activeBtns[0].clicked.connect(lambda: self.setActivePWM(0, activeBtns[0]))
        activeBtns[1].clicked.connect(lambda: self.setActivePWM(1, activeBtns[1]))
        activeBtns[2].clicked.connect(lambda: self.setActivePWM(2, activeBtns[2]))
        activeBtns[3].clicked.connect(lambda: self.setActivePWM(3, activeBtns[3]))
        activeBtns[4].clicked.connect(lambda: self.setActivePWM(4, activeBtns[4]))
        activeBtns[5].clicked.connect(lambda: self.setActivePWM(5, activeBtns[5]))
        activeBtns[6].clicked.connect(lambda: self.setActivePWM(6, activeBtns[6]))
        activeBtns[7].clicked.connect(lambda: self.setActivePWM(7, activeBtns[7]))
        activeBtns[8].clicked.connect(lambda: self.setActivePWM(8, activeBtns[8]))
        activeBtns[9].clicked.connect(lambda: self.setActivePWM(9, activeBtns[9]))
        activeBtns[10].clicked.connect(lambda: self.setActivePWM(10, activeBtns[10]))
        activeBtns[11].clicked.connect(lambda: self.setActivePWM(11, activeBtns[11]))
        activeBtns[12].clicked.connect(lambda: self.setActivePWM(12, activeBtns[12]))
        activeBtns[13].clicked.connect(lambda: self.setActivePWM(13, activeBtns[13]))
        activeBtns[14].clicked.connect(lambda: self.setActivePWM(14, activeBtns[14]))

        scheduBtns[0].clicked.connect(lambda: self.setSchedPWM(0, scheduBtns[0]))
        scheduBtns[1].clicked.connect(lambda: self.setSchedPWM(1, scheduBtns[1]))
        scheduBtns[2].clicked.connect(lambda: self.setSchedPWM(2, scheduBtns[2]))
        scheduBtns[3].clicked.connect(lambda: self.setSchedPWM(3, scheduBtns[3]))
        scheduBtns[4].clicked.connect(lambda: self.setSchedPWM(4, scheduBtns[4]))
        scheduBtns[5].clicked.connect(lambda: self.setSchedPWM(5, scheduBtns[5]))
        scheduBtns[6].clicked.connect(lambda: self.setSchedPWM(6, scheduBtns[6]))
        scheduBtns[7].clicked.connect(lambda: self.setSchedPWM(7, scheduBtns[7]))
        scheduBtns[8].clicked.connect(lambda: self.setSchedPWM(8, scheduBtns[8]))
        scheduBtns[9].clicked.connect(lambda: self.setSchedPWM(9, scheduBtns[9]))
        scheduBtns[10].clicked.connect(lambda: self.setSchedPWM(10, scheduBtns[10]))
        scheduBtns[11].clicked.connect(lambda: self.setSchedPWM(11, scheduBtns[11]))
        scheduBtns[12].clicked.connect(lambda: self.setSchedPWM(12, scheduBtns[12]))
        scheduBtns[13].clicked.connect(lambda: self.setSchedPWM(13, scheduBtns[13]))

        self.activeBtn.clicked.connect(self.showActive)
        self.scheduleBtn.clicked.connect(self.showSchedule)

        self.autotestBtn.clicked.connect(lambda: self.runAutoTest())

        self.statusbar.showMessage('Ready')
        
    # set active pwm channels
    def setActivePWM(self, idx, btn):
        self.chmsl.setPWM(activePWM1[idx], activePWM2[idx])
        self.statusbar.showMessage('Active: {}, PWM1 DC: {}%, PWM2 DC: {}%'.format(btn.text(), activePWM1[idx], activePWM2[idx]))
        btn.setDown(True)

    # set schedule pwm channels
    def setSchedPWM(self, idx, btn):
        self.chmsl.setPWM(schedPWM1[idx], schedPWM2[idx])
        self.statusbar.showMessage('Schedule: {}, PWM1 DC: {}%, PWM2 DC: {}%'.format(btn.text(), schedPWM1[idx], schedPWM2[idx]))
        btn.setDown(True)

    # show active page
    def showActive(self):
        self.stackedWidget.setCurrentIndex(0)
        self.groupBox.setTitle('Active Charging')
        #self.scheduleBtn.setDown(False)
        #self.activeBtn.setDown(True)

    # show schedule page
    def showSchedule(self):
        self.stackedWidget.setCurrentIndex(1)
        self.groupBox.setTitle('Schedule Charging')
        #self.scheduleBtn.setDown(True)
        #self.activeBtn.setDown(False)

    # disable all buttons
    def disAllBtns(self):
        for eachBtn in activeBtns:
            eachBtn.setEnabled(False)
        for eachBtn in scheduBtns:
            eachBtn.setEnabled(False)

    # enable all buttons
    def enAllBtns(self):
        for eachBtn in activeBtns:
            eachBtn.setEnabled(True)
        for eachBtn in scheduBtns:
            eachBtn.setEnabled(True)

    # run autotest procedure
    def runAutoTest(self):
        global autotestThreadExit
        print('Starting Auto Test.\n')
        autotestThreadExit = False
        self.autotestBtn.setText('Stop Auto Test')
        self.autotestBtn.clicked.disconnect()
        self.autotestBtn.clicked.connect(lambda: self.stopAutoTest())

        # separate thread to prevent gui freezing
        thread = threading.Thread(target=self.autoTest, args=())
        thread.daemon = True
        thread.start()
       
        
    # raise exit flag for autotest to stop
    def stopAutoTest(self):
        global autotestThreadExit
        self.statusbar.showMessage('Auto test stopped')
        print('Stopping Auto Test.\n')
        autotestThreadExit = True
        self.autotestBtn.setText('Start Auto Test')
        self.autotestBtn.clicked.disconnect()
        self.autotestBtn.clicked.connect(lambda: self.runAutoTest())


    def autoTest(self):
        print('Auto test thread running...')
        global autotestThreadExit
        self.statusbar.showMessage('Auto test started')
        self.showActive()

        for eachBtn in activeBtns:
            if autotestThreadExit: return
            eachBtn.click()
            eachBtn.setDown(True)
            self.update()
            time.sleep(autotestDelay)
            eachBtn.setDown(False)
            self.update()

        self.showSchedule()
        time.sleep(1)

        for eachBtn in scheduBtns:
            if autotestThreadExit: return
            eachBtn.click()
            eachBtn.setDown(True)
            self.update()
            time.sleep(autotestDelay)
            eachBtn.setDown(False)
            self.update()

        self.autotestBtn.click()
        self.update()
        
##    class autoTest(object):
##        global autotestThreadExit
##        
##        def __init__(self):
##            thread = threading.Thread(target=self.run, args=())
##            thread.daemon = True                
##            thread.start()                                  
##
##        def run(self):
##            global autotestThreadExit
##            statusBar.showMessage('Running auto test')
##            print('Auto test thread running...')
##            
##
##            stackedWidget.setCurrentIndex(0)
##            groupBox.setTitle('Active Charging')
##            
##            x = chmslControl()
##
##            # active charging testing
##            for dc1, dc2, b in zip(activePWM1, activePWM2, activeBtns):
##                if autotestThreadExit:
##                    return                
##                x.setPWM(dc1=dc1, dc2=dc2)
##                #print('dc1: {}, dc2: {}'.format(dc1, dc2))
##                time.sleep(autotestDelay)
##
##            # schedule charging testing
##            for dc1, dc2 in zip(schedPWM1, schedPWM2):
##                if autotestThreadExit:
##                    return                
##                x.setPWM(dc1=dc1, dc2=dc2)
##                #print('dc1: {}, dc2: {}'.format(dc1, dc2))
##                time.sleep(autotestDelay)
##
##            autotestThreadExit = True
       
def main():
    app = QApplication(sys.argv)
    form = chmslBench()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
