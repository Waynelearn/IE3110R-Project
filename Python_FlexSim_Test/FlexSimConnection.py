import subprocess
import socket
class FlexSimConnection():
    def __init__(self, flexsimPath, modelPath, address='localhost', port=5005):
         self.flexsimPath = flexsimPath
         self.modelPath = modelPath
         self.address = address
         self.port = port
         
    def launch_flexsim(self):
         args = [self.flexsimPath, self.modelPath] # option to add aditional arguments
         self.flexsimProcess = subprocess.Popen(args)
         self.init(self.address, self.port)
         
    def close_flexsim(self):
         self.flexsimProcess.kill()
         self.end(self.address, self.port)
         
    def init(self, host, port): 
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((host, port))
        self.serversocket.listen();
        (self.clientsocket, self.socketaddress) = self.serversocket.accept()
        message = self.recv()
        if message != b"READY":
            raise RuntimeError("Did not receive READY! message")
    
    def end(self, host, port):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((host, port))
        self.serversocket.close()
        
    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.clientsocket.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            totalsent = totalsent + sent
    '''   
    def recv(self):
        chunks = []
        while 1:
            chunk = self.clientsocket.recv(2048)
            if chunk == b'':
                raise RuntimeError("Socket connection broken")
            if chunk[-1] == ord('!'):
                chunks.append(chunk[:-1])
                break;
            else:
                chunks.append(chunk)
        return b''.join(chunks)
    '''

    def recv(self):
        msg = self.clientsocket.recv(2048)
        print(f"Message Rev:{msg}")
        if msg == b"":
            raise RuntimeError("Socket connection broken")
        return msg

if __name__ == "__main__":
    pass
        
    
