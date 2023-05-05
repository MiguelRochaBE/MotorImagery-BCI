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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("raspberrypi",5000))


#while frame>0
frame=True
while frame: #valor arbitrariamente elevado (tão elevado quanto mais tempo durar a experiência (claro que podemos mudar e fazer com que pare aquando de um dado comando))
    print(int(s.recv(1024).decode("utf-8")))


    """#number = clf.predict(#read a file here from EEG signals) #assumindo que as classificações vêm como "0,1,2,3,4" (se não, é só mudar)"""
    """if frame<1000:
        number=0

    if 1000<frame<2000:
        number=1

    if 2000<frame<3000:
        number=2
    
    if 3000<frame<4000:
        number=3
    
    if 4000<frame<5000:
        number=4"""

    """#test insert number
    number = int(input("Movement: "))
    print(number)
    print("\n")

    '''
    if ultra.getDistance()<=0.3: #se a distância for inferior a 2(metros?)
        control.stop() #parar
        
        #impedir que continue a mover-se para a frente; só pode efetuar as restantes ações:
        if number==0: #If it classifies as 0, the robot is at rest
            control.stop()

        if number==2: #walk backward
            control.backWard()
            control.stop()

        if number==3: #raise height
            control.upAndDown(1) #este? Ou o postureBalance?
            control.stop()
        
        if number==4: #lower height
            control.upAndDown(-1)
            control.stop()
        
        #buzz.run(1) #começa a ladrar indefinidamente
        
        alert=1
    
    else:
        #buzz.run(0) #para de ladrar
        alert=0 
     '''
   
    alert = 0
    if alert==0: #dog can move forward, when alert flag is 0
        
        if number==0: #If it classifies as 0, the robot is at rest
            control.stop()
        
        if number==1: #If it classifies as 1, walk forward
            control.forWard() #one step forward
            #control.stop()
            print("forWard")

        if number==2: #walk backward
            control.backWard()
            #control.stop()
            print("backWard")

        if number==3: #raise height
         control.upAndDown(1) #este? Ou o postureBalance?
            control.stop()
            print("upAndDown")
            
        if number==4: #lower height
            control.upAndDown(-1)
            control.stop()
            print("upAndDown")"""
            
        #seria engraçado se uma das indicações mudasse as instruções
        #passando de frente e trás, para esquerda e direita.
    #control.stop()
    #frame+=1
    #time.sleep(0.1) #to be changed, depending on how the robot actually operates
    """


#control.stop()"""