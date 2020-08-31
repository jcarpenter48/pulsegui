from tkinter import *
#main import for gui features
import subprocess

from stylegan import G_synthesis,G_mapping
from dataclasses import dataclass
from SphericalOptimizer import SphericalOptimizer
from pathlib import Path
import numpy as np
import time
import torch
from loss import LossBuilder
from functools import partial
from drive import open_url

from PULSE import PULSE
from torch.utils.data import Dataset, DataLoader
from torch.nn import DataParallel
from pathlib import Path
from PIL import Image
import torchvision
from math import log10, ceil
import argparse
#libraries needed for PULSE to operate
import os
#for executing PULSE scripts
       
window = Tk()
window.title("PULSE GUI App")
window.geometry('640x480')

lblWelcome = Label(window, text="  Welcome to the PULSE GUI  ", font=("Arial Bold", 30))
lblWelcome.config(anchor=CENTER)
        
text = Text(window)
#text.insert(END, "this is a test")

def clickedAnalyze():
    text.insert(END, "Analyzing and Aligning Faces..."+'\n')
    #os.system("python align_face.py")
    #os.system('exit')
    p = subprocess.Popen(["python.exe","./align_face.py"], stdout=subprocess.PIPE)
    out = p.stdout.read()
    text.insert(END, out+b'\n')
    text.insert(END, "Faces aligned. Ready to Run PULSE."+'\n')
        
btnAnalyze = Button(window, text="Analyze Faces", bg="white",fg="black", command=clickedAnalyze)
        
def clickedRun():
    text.insert(END, "Executing PULSE..."+'\n')    
    #os.system("python run.py -eps 8e-3")
    #os.system('exit')
    p = subprocess.Popen(["python.exe","./run.py"], stdout=subprocess.PIPE)
    out = p.stdout.read()
    text.insert(END, out+b'\n')
    text.insert(END, "New faces generated. Check output folder for results."+'\n')    
            
btnRun = Button(window, text="   Run PULSE   ", bg="black",fg="white", command=clickedRun)
        
        
lblWelcome.pack()
text.pack()
btnAnalyze.pack(side='left')        
btnRun.pack(side='right')
        
window.mainloop()
        
#end