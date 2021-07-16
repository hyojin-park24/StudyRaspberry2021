#온습도 센서 
import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 4

try:
    while True:
        (h, t) = dht.read_retry(sensor, pin)
        if h != None and t != None:
            print('Temp = {0}C / Humidity = {1}%'.format(t,h))
        else:
            print('Sesing error')

            time.sleep(1)
except Exception as e:
    print('Error occured : {0}'.format(e))
finally:
    print('End of progra')