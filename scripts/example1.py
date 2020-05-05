from win32api import GetSystemMetrics
import numpy as np
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from graphics import *
from disk_expansions import *

# get width and height automatically from system
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# or overwrite for another target display
# width = 1920
# height = 1080
    
def main():

    # define frame rate
    FR = 30
    
    # stimulus is centred on screen
    x = width/2
    y = height/2
    
    # stimulus size 
    r0 = 33.9                               # initial radius
    rf_l = 339                              # final radius 
    
    # stimulus timing
    SS = FR * 3                             # end of stable small period
    EX = SS + FR * 2                        # end of expansion period
    SL = EX + FR * 3                        # end of stable large period
    
    # expansion rate
    er_lin = ( rf_l - r0 ) / ( EX - SS )    
    
    win = GraphWin("LVS Example 1", width, height)
    win.setBackground("white")
    
    print('Click window to start shadow expansion series:')
    win.getMouse()
    
    #shadow loom #0    
    for i in range(0,10):
        c = exp_lin(x,y,r0,er_lin,win,SL,SS,EX,FR)
        remove(c)
        wait(FR,2)
        i += 1
    
    win.close()    # Close window when done

main()