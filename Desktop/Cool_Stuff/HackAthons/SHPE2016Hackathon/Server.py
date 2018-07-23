# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:26:00 2016

@author: Jose
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:31:42 2016

@author: Jose
"""
import socket
import datetime
import random
import time

# Import socket module
#!/usr/bin/python           # This is server.py file

             # Import socket module
            # Close the connection





def random_Heartbeat():  # since we dont have acess to actual hardware, we are simulating the heartbeat through a random function
    heartbeat_average = 108
    random_number = random.random()
    if random_number >= .5:
        if .80 > random_number >= .75:
            heartbeat_average += 9
        else:
            heartbeat_average += 3
    elif random_number < .5:
        if .30 > random_number >= .25:
            heartbeat_average -= 9
        else:
            heartbeat_average -= 3
    elif heartbeat_average < 40:
        return heartbeat_average
    elif heartbeat_average > 145:
        return heartbeat_average
    return heartbeat_average


def random_Temp():  # since we dont have acess to actual hardware, we are simulating the temperature through a random function
    body_Temp_average = 98
    random_number_2 = random.random()
    if random_number_2 >= .5:
        if .80 > random_number_2 >= .75:
            body_Temp_average += 1.5
        else:
            body_Temp_average += .5
    elif random_number_2 < .5:
        if .3 > random_number_2 >= .25:
            body_Temp_average -= 1.5
        else:
            body_Temp_average -= .5
    if body_Temp_average > 102:
        return body_Temp_average
    if body_Temp_average < 95:
        return body_Temp_average
    return body_Temp_average
class VitalMonitor:
    def __init__(self, Heartbeat, Temp , subject ):  # gets the variable info and stores them in their suitable variable
        self.Heartbeat = Heartbeat
        self.Temp = Temp
        self.subject = subject

    def set_Heartbeat(self, hb):
        self_Heartbeat = hb
    def set_Temp(self, t):
        self_Temp = t
    def get_hBeat(self):
        return self.Heartbeat

    def get_temp(self):
        return self.Temp

    def logging(self, s):
        outfile = open("logs.txt", "w")
        outfile.write(s)

        outfile.close()

    def check_Heartbeat(self):
        if 145 < self.Heartbeat:  # acceptable heartrate for an active adult is from 114-145
            self.logging("[" +str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))+"]" + "Subject " + str(self.subject)+"has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp())+  " WARNING: Heart Beat\n")
        elif self.Heartbeat <= 145 and self.Heartbeat >= 120:
            self.logging("[" + str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))+"]" + "Subject " + str(self.subject)+ "has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp())+ " Caution: Heart Beat\n")
        else:
            self.logging("[" +str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))+ "]"+ "Subject " + str(self.subject)+ "has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp()) + "\n" )

            # print ("subject " +self.subject+ " has a heartrate of: "+ self.Heartbeat+" bpm." )

    def check_Temp(self):
        if 102 > self.Temp and self.Temp >= 99:  # acceptable body temperature is from 97-99 degrees fahrenheit in the regular adult.
            self.logging("[" + str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))+"]" + "Subject " + str(self.subject)+ "has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp())+ " CAUTION: Body Temperature\n")
        # print("subject " +self.subject+ " has a body temperature of: "+ self.Temp+" Fahrenheit.")
        elif self.Temp >= 102:
            self.logging("[" + str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))+ "]"+ "Subject " + str(self.subject)+ " has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp())+  " WARNING: Body Temperature\n")
        else:
            self.logging("["+str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) + "]" + "Subject " + str(self.subject)+ " has HeartBeat: " + str(self.get_hBeat()) + " and Body Temperature: "+str(self.get_temp()) + "\n")






if __name__ == "__main__":
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 30300  # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port

    s.listen(5)  # Now wait for client connection.
    while True:
        c, addr = s.accept()  # Establish connection with client.
        print ('Got connection from', addr)
        heartbeat_sig = c.recv(1024).decode()
        temperature_sig = c.recv(1024).decode()
        hb_log = []
        t_log = []
        test = VitalMonitor(heartbeat_sig, temperature_sig, 0)
        hb_log.append(heartbeat_sig)
        t_log.append(temperature_sig)
        print(t_log)
        print(hb_log)
        test.check_Heartbeat()
        test.check_Temp()
        c.close()






