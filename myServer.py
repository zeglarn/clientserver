from time import sleep
from clientserver import Server
from instr import *
import pickle

def main():
    myServer = Server()

    while True:
        message = myServer.recv()
        if message:
            myInstr = pickle.loads(message)
            myInstr.printSelf()
            if myInstr.quit == True:
                break

    myServer.disconnect()

main()
