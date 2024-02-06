'''
Control the Brightness of LED using PWM on Raspberry Pi
http://www.electronicwings.com
'''

import RPi.GPIO as GPIO
from time import sleep

ledpin = 12				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,500)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
while True:
  pi_pwm.ChangeDutyCycle(100) #provide duty cycle in the range 0-100
  sleep(3)
  pi_pwm.ChangeDutyCycle(0)
  sleep(3)
