#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import random
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 30300                # Reserve a port for your service.
s.connect((host, port))
    # Establish connection with client.
def random_Heartbeat():# since we dont have acess to actual hardware, we are simulating the heartbeat through a random function
        heartbeat_average = 80
        random_number = random.random()
        if random_number >= .5:
            if .80>random_number>=.75:
                heartbeat_average += 9
            else:
                heartbeat_average += 3
        elif random_number < .5:
            if .30>random_number>=.25:
                heartbeat_average -= 9
            else:
                heartbeat_average -= 3
        elif heartbeat_average < 40:
            return hearbeat_average
        elif heartbeat_average > 145:
            return heartbeat_average
        return heartbeat_average
        
def random_Temp(): # since we dont have acess to actual hardware, we are simulating the temperature through a random function
    body_Temp_average= 95
    random_number_2 = random.random()
    if random_number_2 >= .5:
        if .80>random_number_2>=.75:
            body_Temp_average += 1.5
        else:
            body_Temp_average += .5
    elif random_number_2 < .5:
        if .3>random_number_2>=.25:
            body_Temp_average -= 1.5
        else:
            body_Temp_average -= .5
    if body_Temp_average > 102:
        return body_Temp_average
    if body_Temp_average< 95:
        return body_Temp_average
    return body_Temp_average

Heartbeat= str(random_Heartbeat())
Temperature = str(random_Temp())
s.sendto(Heartbeat.encode(),(host,port))
s.sendto(Temperature.encode(),(host,port))
s.close()
                     # Close the socket when done
