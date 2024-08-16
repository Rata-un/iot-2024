import asyncio
import websockets
import RPi.GPIO as GPIO

# Define the GPIO pin connected to your switch
switch_pin = 17

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

async def main():
    uri = "ws://172.20.10.10:8765"
    async with websockets.connect(uri) as websocket:
        print("Connect to Server")

        async def send_switch_state():
            while True:
                # Get the current state of the switch
                switch_state = GPIO.input(switch_pin)
                # Send the state as a string
                await websocket.send(str(switch_state))
                # Print the state to the terminal
                print(f"Sending switch state: {switch_state}")
                # Add a small delay to avoid sending too frequently
                await asyncio.sleep(0.5)

        async def recieve_message():
            while True:
                try:
                    message = await websocket.recv()
                    print(f"Recieve : {message}")
                except websockets.exceptions.ConnectionClosed:
                    print("Conection Closed")
                    break

        await asyncio.gather(send_switch_state(), recieve_message())

if __name__ == "__main__":
    asyncio.run(main())