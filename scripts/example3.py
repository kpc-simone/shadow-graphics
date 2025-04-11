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
    
    # stimulus sweeps diagonally across the screen
    xi = width * 0.1
    yi = height * 0.1
    xf = width * 0.9
    yf = height * 0.9
    
    # stimulus size
    r0 = 33.9                               # radius
    
    # stimulus timing
    SD = FR * 8                             # frames needed to complete a sweep segment
    
    # linear sweep rate
    sr_lin_x = ( xf - xi ) / SD
    sr_lin_y = ( yf - yi ) / SD
    
    win = GraphWin("LVS Example 2", width, height)
    win.setBackground("gray")
    
    print('Click window to start shadow expansion series:')
    win.getMouse()
    
    # shadow loom #4
    c = sweep(xi,yi,sr_lin_x,sr_lin_y,r0,win,SD,FR)
    #remove(c)
    wait(FR,2)
    
    win.close()    # Close window when done

main()