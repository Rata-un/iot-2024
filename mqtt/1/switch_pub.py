import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

switch_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mqttc = mqtt.Client()
mqttc.connect("broker.mqttdashboard.com", 1883)

while True:
        switch_state = GPIO.input(switch_pin)
        if switch_state == 0:
            mqttc.publish("test/enfant", "on")
            print("Switch pressed, sent 'on'")
        elif switch_state == 1:
            mqttc.publish("test/enfant", "off")
            print("Switch pressed, sent 'off'")
        time.sleep(2)
