import argparse
import requests
import time
import RPi.GPIO as GPIO

ACCESS_KEY = ""
URL = f"https://www.divera247.com/api/v2/alarms?accesskey={ACCESS_KEY}"
DATA = {
    'Alarm': 
    {
        'priority': 'true',
        'title': 'Melderalarmierung!', 
        'text': 'Alarmierung über Melder erkannt, weitere Infos folgen.', 
        'notification_type': 0, 
        'send_push': 'true', 
        "send_pager": 'true', 
        'type': 'string', 
        'uploads': 'Binary'
    }
}


GPIO.setmode(GPIO.BOARD)
GPIO.setup(1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.add_event_detect(1, GPIO.FALLING, callback=ALAAAAARM, bouncetime=300)  


def main():
    while(True):
        time.sleep(10000)

def ALAAAAARM(channel):
    result = requests.post(URL, json=DATA)
    print(result.status_code)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
