import socket
import threading
from queue import Queue


target = input("input the target IP address for the scan: ")
queue = Queue()
openPorts = []

def fillQueue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open".format(port))
            openPorts.append(port)


def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


portList = range(1,1500)
fillQueue(portList)

threadList = []

for t in range(200):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()

print("Open ports are: ", openPorts)