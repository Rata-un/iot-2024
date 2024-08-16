import time
import spidev
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

LED_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 1000)  # Set PWM frequency to 1kHz
pwm.start(0)  # Start PWM with 0% duty cycle (LED off)

def ReadChannel(channel):
    r = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    return ((r[1] & 15) << 8) + r[2]

while True:
    reading = ReadChannel(0)
    voltage = reading * 3.3 / 4096
    duty_cycle = (reading / 4096) * 100
        
    print("Reading=%d\t Voltage=%.2f\t Duty Cycle=%.2f" % (reading, voltage, duty_cycle))
    pwm.ChangeDutyCycle(duty_cycle) 
        
    time.sleep(1.5)
