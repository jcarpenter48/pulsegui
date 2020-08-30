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

class MainApplicationGUI():
        # constructor of Main class 
        def __init__(self): 
            self.String1="Hello"
        
        window = Tk()
        window.title("PULSE GUI App")
        window.geometry('640x480')

        lblWelcome = Label(window, text="  Welcome to the PULSE GUI  ", font=("Arial Bold", 30))
        lblWelcome.config(anchor=CENTER)
        
        txt = Text(master=None)

        #terminal output in a text widget
        def redirect(module, method):
            proc = subprocess.Popen(["python", "-c",
                "import " + module + ";" + module + "." + method + "()"], stdout=subprocess.PIPE)
            out = proc.communicate()[0]
            return out.decode('unicode_escape')
        
        def put_in_txt():
            txt.insert('1.0', redirect(module.get(), method.get()))
        ###################
        def clickedAnalyze():
            os.system("python align_face.py")
            os.system('exit')
            window.update()
        
        btnAnalyze = Button(window, text="Analyze Faces", bg="white",fg="black", command=clickedAnalyze)
        
        def clickedRun():
            os.system("python run.py -eps 8e-3")
            os.system('exit')
            
        btnRun = Button(window, text="   Run PULSE   ", bg="black",fg="white", command=clickedRun)
        
        
        lblWelcome.pack()
        txt.pack()
        btnAnalyze.pack(side='left')        
        btnRun.pack(side='right')
        
        window.mainloop()
        
#end class MainApplicationGUI