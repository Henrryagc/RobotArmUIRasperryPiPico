from time import sleep

import serial

class Connect:
    def __init__(self):
        try:
            print("Connect to Arduino One, Wait please...!")
            #self.board = serial.Serial('COM3', 9800, timeout=.1)
            #sleep(2)
            print("Connected...") 
        except:
            print("Connection error...")

