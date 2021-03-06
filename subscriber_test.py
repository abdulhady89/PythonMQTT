import paho.mqtt.client as mqtt
broker="test.mosquitto.org"
port=1883

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/coba")

def on_message(client, userdata, msg):
  print(msg.payload.decode())
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()
    
client = mqtt.Client()
client.connect(broker,port,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
