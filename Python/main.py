import RPi.GPIO as GPIO
import time
import sys
import traceback
from SendMail import SendMail #importuju ze skriptu pokus.py metodu SendMail
import picamera	
import datetime
from pushetta import Pushetta

def get_file_name():
     return datetime.datetime.now().strftime("/home/pi/Detector/photo/%Y-%m-%d_%H.%M.%S.jpg")

def main():
 try:
  sensor = 4

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

  previous_state = False
  current_state = False
  cam = picamera.PiCamera()

  API_KEY="e224478433d166114af5e762433790fb5f5921a5"
  CHANNEL_NAME="CzechBery"
  p=Pushetta(API_KEY)
  print "...Camera trap is ready... "

  while True:
      time.sleep(0.1)
      previous_state = current_state
      current_state = GPIO.input(sensor)
      if current_state != previous_state:
          new_state = "HIGH" if current_state else "LOW"
          print("GPIO pin %s is %s" % (sensor, new_state))
          if current_state:
              fileName = get_file_name()
              cam.start_preview()
              p.pushMessage(CHANNEL_NAME, "Motion Detected... Look at mail!")
              time.sleep(2)
              cam.capture(fileName)
              time.sleep(1)
              SendMail(fileName)#zde volam na metodu SendMail a pridavam ji atribut filname coz je nazev souboru ktery se ma poslat mailem
          else:
              cam.stop_preview()
 except KeyboardInterrupt:
     print " System is terminated"
 except Exception:
     print "Nastal Error"

if __name__ ==
    main()
