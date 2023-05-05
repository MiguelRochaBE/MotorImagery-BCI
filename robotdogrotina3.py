# -*- coding: utf-8 -*-
"""RobotDogRotina.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEG1wqeP6KNbJBlVdhigaq9-t_MEyzpf
"""
import socket
import time
from threading import Timer
from Control import *
from Ultrasonic import *
from Buzzer import *

# Create object
control = Control()
ultra = Ultrasonic()
buzz = Buzzer()
number=-1

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 5000))
s.listen(1)
print("Waiting for a connection...")

conn, addr = s.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode("utf-8")
    print("Received message:", message)
    response = "Thanks for your message: " + message
    conn.send(response.encode("utf-8"))
