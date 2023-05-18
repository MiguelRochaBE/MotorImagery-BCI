# -*- coding: utf-8 -*-
"""RobotDogRotina.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEG1wqeP6KNbJBlVdhigaq9-t_MEyzpf
"""
import socket
import time
from threading import Timer
from  Dog_Routines.Control import *
from  Dog_Routines.Ultrasonic import *
from  Dog_Routines.Buzzer import *
from  Dog_Routines.Servo import *

# Create object
control = Control()
ultra = Ultrasonic()
buzz = Buzzer()
servo = Servo()
number=-1

buzz.run(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(5)
print('Server is now running.')

conn, addr = s.accept()
print("Connected by", addr)

flag=0

uppie=2
downie=-2
uppie2=20
downie=-20

control.speed(5)
#control.

#buzz.run(0) #certificar que o buzzer está desligado #USAR ESTE
while True: 
    time_beg=0
    data = conn.recv(1024)
    number = int(data.decode("utf-8"))
    
    distance = ultra.getDistance() #a distância é em centímetros (eles fazem pingTime * 340.0 / 2.0 /10000.0)
    # pingTime = (pulseTime = (time.time() - t0)*1000000); estando em us (time é em s)
    # 340 m/s é a velocidade do som
    # 2 é a dividir a distância ida e volta
    # 10000 = (1/1000000 [us para s]) * (100 [m para cm]); convertendo para cm
        
    if distance <=20: #se estiver a menos de 20 centímetros de um obstáculo
        
        #buzz.run(1) #USAR ESTE
        t0 = time.time()
        pode_sair = 0
        while distance <=5: #se algo estiver a menos de 5 centímetros do cão durante mais de um segundo, a flag muda
            if (time.time()-t0>=1) and pode_sair==0:
                #print ("Distance less than 5 cm for over 1 sec")
                flag = flag+1
                #time.sleep(200) #ms
                #buzz.run(1)
                pode_sair=1
            distance = ultra.getDistance()

        if flag%2 == 0: #se a flag for par, tem um certo conjunto de movimentos
            if number==0: #If it classifies as 0, the robot is at rest
                control.stop()

            if number==1: #If it classifies as 1, it won't walk forward; instead, it will nod in disagreement
                servo.setServoAngle(15,161) #first rotate head to one side #acho que "15" é o servo da cabeça
                #time.sleep(1) #é preciso sleep?
                servo.setServoAngle(15,19) #then rotate it to the other
                #time.sleep(1)
                servo.setServoAngle(15,90) #then go back to standard position #não sei se 19, 161 e 90 estão bem
                #print("forWard")

            if number==2: #walk backward
                
                while (time.time() - time_beg)<=2:
                    control.backWard()
                    #print("backWard")
                control.stop()

            if number==3: #raise height
                
                while (time.time() - time_beg)<=2:
                    control.upAndDown(uppie) #este? Ou o postureBalance?
                    print("upAndDown")
                    
                control.stop()

            if number==4: #lower height
                
                while (time.time() - time_beg)<=2:
                    control.upAndDown(downie)
                    print("upAndDown")
                control.stop()

        if flag%2 != 0: #se a flag for ímpar, tem um diferente conjunto de movimentos
            if number==0: #If it classifies as 0, the robot is at rest
                
                while (time.time() - time_beg)<=2:
                    control.stop()

            if number==1: 
                while (time.time() - time_beg)<=2:
                    control.turnLeft() #one step forward
                    print("turnLeft")
                control.stop()

            if number==2: #walk backward
                while (time.time() - time_beg)<=2:
                    control.turnRight()
                    print("turnRight")
                control.stop()

            if number==3: #raise height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(uppie2) #este? Ou o postureBalance? Ou attitude?
                    print("upAndDown")
                control.stop()

            if number==4: #lower height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(downie2)
                    print("upAndDown")
                control.stop()
        
#         # Stop the robot
#         control.order[0] = cmd.CMD_STOP
#         control.run()
        
            
    else: #se estiver a mais de 20 centímetros de um obstáculo (código praticamente igual a <20cm, mas agora com o forWard incluído)
        #buzz.run(0) #certificar que está calado #USAR ESTE
        
        if flag%2 == 0: #se a flag for par, tem um certo conjunto de movimentos
            if number==0: #If it classifies as 0, the robot is at rest
                while (time.time() - time_beg)<=2:
                    control.stop()
                
            if number==1: #If it classifies as 1, walk forward
                while (time.time() - time_beg)<=2:
                    control.forWard()
                control.stop()
                
                #Tentar isto:
                # Set the command to move forward
                #control.order[0] = cmd.CMD_MOVE_FORWARD
                #control.order[1] = '8'  #with a speed of 8
                # Start the robot
                #control.run()
                
                #time.sleep(2) #walk forward for 2 seconds
                
                #print("forWard")

            if number==2: #walk backward
                while (time.time() - time_beg)<=2:
                    control.backWard()
                    print("backWard")
                control.stop()
                    

            if number==3: #raise height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(uppie) #este? Ou o postureBalance?
                    print("upAndDown")
                control.stop()

            if number==4: #lower height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(downie)
                    print("upAndDown")
                control.stop()
    
        if flag%2 != 0: #se a flag for ímpar, tem um diferente conjunto de movimentos
            
            if number==0: #If it classifies as 0, the robot is at rest
                while (time.time() - time_beg)<=2:
                    control.stop()

            if number==1:
                while (time.time() - time_beg)<=2:
                    control.turnLeft()
                    print("turnLeft")
                control.stop()

            if number==2:
                while (time.time() - time_beg)<=2:
                    control.turnRight()
                    print("turnRight")
                control.stop()

            if number==3: #raise height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(uppie2) #este? Ou o postureBalance?
                    print("upAndDown")
                control.stop()

            if number==4: #lower height
                while (time.time() - time_beg)<=2:
                    control.upAndDown(downie2)
                    print("upAndDown")
                control.stop()
                
        # Stop the robot
        #control.order[0] = cmd.CMD_STOP
        #control.run()
        #control.stop()
'''        
import math
from Control import *
from Servo import *
class Fidalction:
    def __init__(self):
        self.servo=Servo()
        self.control=Control()
        self.servo.setServoAngle(15,90)
    def jump_dalgo(self):
        xyz=[[0,50,0],[-100,23,0],[-100,23,0],[0,50,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
        for i in range(4):
            for i in range(50,120,1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
            for i in range(120,50,-1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
'''