import time
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel): 
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    return data
 
while True:
    reading = ReadChannel(0)
    voltage = reading * 3.3 /4096
    temp = reading
    print("Reading=%d\t Voltage=%f" % (reading, voltage))
    time.sleep(1)

# import time
# import spidev

# spi = spidev.SpiDev()

# spi.open(0,0)

# def anaread(channel):
#     r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])
#     adc_out = ((r[1]&15) << 8) + r[2]
#     return adc_out

# while True:
#     reading = anaread(0)
#     voltage = reading * 3.3 / 4096
#     Temp = voltage * 99.5
#     print("Reading=%d\tVoltage=%f\tTemp=%2.2f" % (reading, voltage,Temp)) 
#     time.sleep(1)