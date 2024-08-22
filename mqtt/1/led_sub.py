import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

MQTT_BROKER = 'mqtt-dashboard.com'  
MQTT_PORT = 1883
MQTT_TOPIC = 'test/enfant'

switch_pin = 4

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.OUT)

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Received message '{payload}' on topic '{message.topic}'")
    if payload == "on":
        GPIO.output(switch_pin, GPIO.HIGH)  # Turn the switch on
        print("Switch turned ON")
    elif payload == "off":
        GPIO.output(switch_pin, GPIO.LOW)  # Turn the switch off
        print("Switch turned OFF")

# Create a new MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

try:
    # Keep the script running
    while True:
        pass
except KeyboardInterrupt:
    # Stop the loop and disconnect gracefully on keyboard interrupt
    client.loop_stop()
    client.disconnect()
