#온습도 센서2 (처음거 오류나서 다시 만듦)
import RPi.GPIO as GPIO
import dht11
import time

pin = 4
GPIO.setwarnings(False)     ## error message block
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin)    ##dht11 인스턴스 생성

while True:
    try:
        result = instance.read()

        if result.is_valid():
            print('temp : {0}C / Humidity : {1}'.format(result.temperature, result.humidity))
        else:
            print('Read error : {0}'.format(result.error_code))

        time.sleep(2)
    except Exception:
        GPIO.cleanup()