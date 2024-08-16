import RPi.GPIO as GPIO
import time

# ตั้งค่า GPIO ให้ใช้หมายเลข BCM
GPIO.setmode(GPIO.BCM)

# กำหนดพิน TRIG และ ECHO
TRIG = 23
ECHO = 24

# ตั้งค่าพิน TRIG เป็นเอาท์พุต และพิน ECHO เป็นอินพุต
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # ทำให้พิน TRIG เป็น Low และรอให้เซนเซอร์พร้อม
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    # ส่งสัญญาณไปที่พิน TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # สูงเป็นเวลา 10 ไมโครวินาที
    GPIO.output(TRIG, False)

    # วัดเวลาเมื่อ ECHO เป็น High
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # คำนวณระยะทางจากเวลาที่วัดได้
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # คำนวณระยะทาง (cm)
    distance = round(distance, 2)  # ปัดเศษทศนิยม 2 ตำแหน่ง

    return distance

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    time.sleep(1)
