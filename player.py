import socket
import threading
import time

import gameBoard 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys  
import json
import socket


class NetworkConfig:
    def __init__(self,  playerName):
        self.playerName = playerName
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.settimeout(5) # 5s
        self.host = "localhost" # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = 8080
        self.addr = (self.host, self.port)
        self.id = self.connect()
        self.connected = False
        
    def connect(self):
        try:
            print("{} is trying to connect to the server...".format(self.playerName))
            self.client.connect(self.addr)
        except:
            print("Could not make a connection to the server")
            input("Press enter to quit")
            sys.exit(0)

        return self.client.recv(2048).decode()

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = json.loads(self.client.recv(2048).decode())
            return reply # in json
        except socket.error as e:
            return str(e)
    
    def recv(self):
        try:
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)        

class Player:
    def __init__(self,name):
        self.playerName = name
        self.net = NetworkConfig(self.playerName)
        self.signal = True
        self.connected = False
       
    
    def run(self):
        if self.net.id == "connected":
            print("Player game status: ", self.net.id)
    
            received = self.net.recv()
            
            if received != "":
                print("Received (from Server): {}\n".format(received))
                
                if received == "start" or "start_first":
                    print("Game is starting\n")
                    if received == "start_first":
                        print("I am starting first\n")    
                    print("Starting GUI...")
                    self.run_gui()
                else:
                    print("Wait to start...")
            else:
                print("Empty package\n")    
            
    def run_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = gameBoard.Ui_MainWindow(self.net, self.playerName)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
