import paho.mqtt.client as mqttClient
import time
import os
import socket
import ssl
from time import sleep
from random import uniform
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "34.221.180.238"
port = 1883
user = "peppomela"
password = "peppomela"
 
client = mqttClient.Client("Pythonsdf")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:
        sleep(5)
        tempreading = uniform(20.0,25.0)
        client.publish("test", tempreading, qos=1)
        print("msg sent: temperature " + "%.2f" % tempreading )
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()
