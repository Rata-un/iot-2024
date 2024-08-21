import asyncio
import websockets
import time
import spidev
import RPi.GPIO as GPIO

# SPI setup
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# GPIO setup
#LED_PIN = 14
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT)
#pwm = GPIO.PWM(LED_PIN, 1000)  # Set PWM frequency to 1kHz
#pwm.start(0)  # Start PWM with 0% duty cycle (LED off)

def ReadChannel(channel):
    r = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    return ((r[1] & 15) << 8) + r[2]

async def main():
    uri = "ws://172.20.10.10:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to Server")
        
        async def send_switch_state():
            while True:
                reading = ReadChannel(0)
                voltage = reading * 3.3 / 4096
                duty_cycle = (reading / 4096) * 100
                
                print(f"Reading={reading}\t Voltage={voltage:.2f}V\t Duty Cycle={duty_cycle:.2f}%")
                #pwm.ChangeDutyCycle(duty_cycle)  # Adjust LED brightness
                await websocket.send(f"{voltage:.2f}")  # Send voltage to server
                await asyncio.sleep(0.5)

        async def receive_message():
            while True:
                try:
                    message = await websocket.recv()
                    print(f"Received: {message}")
                except websockets.exceptions.ConnectionClosed:
                    print("Connection Closed")
                    break

        await asyncio.gather(send_switch_state(), receive_message())

if __name__ == "__main__":
    asyncio.run(main())
