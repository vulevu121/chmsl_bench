import tkinter as tk
from PIL import ImageTk,Image
import time
from subprocess import call
import pigpio
import threading


chmslFreq = 200
pwm1Pin = 17
pwm2Pin = 18


activePWM1 = [ 0, 10, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40]
activePWM2 = [ 0,  0,  0,  6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86,  0]

schedPWM1  = [ 0, 10, 20, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50] 
schedPWM2  = [ 0,  0,  0,  6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86]

autoTestThreadExit = False

class chmslControl():
    def __init__(self):
        print('initializing...')
        # initialize pigpio        
        self.pi = pigpio.pi()
        
        # must initalize pwm1, but pwm2 is not needed
        self.initPWM1()

    
    # initialize pwm1 and set dc range to 0-100
    # software pwm requires initialization
    def initPWM1(self, freq=chmslFreq):
        print('PWM1 initiated.')
        self.pi.set_PWM_frequency(pwm1Pin, freq)
        self.pi.set_PWM_range(pwm1Pin, 100)
        
    # set pwm1 with desired duty cycle, software pwm
    # frequency can only one of 18 discrete values, please see pigpgio reference
    def setPWM1(self, duty, freq=chmslFreq):
        self.pi.set_PWM_frequency(pwm1Pin, freq)
        self.pi.set_PWM_dutycycle(pwm1Pin, (duty))
        print('PWM_1 Duty Cycle: {}%'.format(duty))

    # set pwm2 with desired duty cycle
    # hardware pwm, does not require initialization
    def setPWM2(self, duty, freq=chmslFreq):
        self.pi.hardware_PWM(pwm2Pin, freq, (duty)*10000)
        print('PWM_2 Duty Cycle: {}%'.format(duty))

    # sets both pwm1 and pwm2 channels to desired duty cycles
    def setPWM(self, dc1, dc2):
        self.setPWM1(duty=dc1)
        self.setPWM2(duty=dc2)

    # set both pwm signals to 0 and release pigpio resources
    def stopPWM(self):
        self.pi.set_PWM_dutycycle(pwm1Pin, 0)
        self.pi.set_PWM_dutycycle(pwm2Pin, 0)
        self.pi.stop()
