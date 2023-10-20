from FlexSimConnection import *
import os

flexsimPath = r"C:\Program Files\FlexSim 2022\program\flexsim.exe"
modelPath = r"C:\Users\Wayne Linn\OneDrive\Desktop\Y4S1\IE3110R\Project\Python_Implementation\Python_FlexSim_Test\MM1.fsm"
        
host = "127.0.0.1"
port = 5005
conn = FlexSimConnection(flexsimPath,modelPath,address=host, port=port)
        
print(f"Launching Flexsim...")
conn.launch_flexsim()
        
print("Initiate connection with FlexSim")
print("Awaiting msg")
msg = conn.recv()
print(msg)
#conn.close_flexsim()
