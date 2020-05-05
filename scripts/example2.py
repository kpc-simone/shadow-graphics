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
    rf_l = 339                              # final radius - linear expansion
    rf_e = 372.9                            # final radius - exponesional expansion
    
    # stimulus timing
    SS = FR * 3                             # end of stable small period
    EX = SS + FR * 2                        # end of expansion period
    SL = EX + FR * 3                        # end of stable large period
    
    # linear expansion rate
    er_lin = ( rf_l - r0 ) / ( EX - SS )
    
    # exponential expansion rate
    n = 5
    er_exp = ( 1 / ( EX - SS ) ** n ) * np.log ( rf_e / r0 )
    
    win = GraphWin("LVS Example 2", width, height)
    win.setBackground("white")
    
    print('Click window to start shadow expansion series:')
    win.getMouse()
    
    #shadow loom #-1
    c = exp_lin(x,y,r0,er_lin,win,SL,SS,EX,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #0
    c = exp_lin(x,y,r0,er_lin,win,SL,SS,EX,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #2
    c = exp_sig(x,y,r0,rf_e,er_exp,win,SL,SS,EX,FR,n)
    remove(c)
    wait(FR,2)
    
    #shadow loom #4
    c = stable(x,y,rf_l/2,win,SL,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #1 
    c = exp_exp(x,y,r0,er_exp,win,SL,SS,EX,FR,n)
    remove(c)
    wait(FR,2)
    
    #shadow loom #3
    c = red_lin(x,y,rf_l,er_lin,win,SL,SS,EX,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #0
    c = exp_lin(x,y,r0,er_lin,win,SL,SS,EX,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #3
    c = red_lin(x,y,rf_l,er_lin,win,SL,SS,EX,FR)
    remove(c)
    wait(FR,2)
    
    #shadow loom #1 
    c = exp_exp(x,y,r0,er_exp,win,SL,SS,EX,FR,n)
    remove(c)
    wait(FR,2)
    
    #shadow loom #2
    c = exp_sig(x,y,r0,rf_e,er_exp,win,SL,SS,EX,FR,n)
    remove(c)
    wait(FR,2)
    
    #shadow loom #4
    c = stable(x,y,rf_l/2,win,SL,FR)
    remove(c)
    wait(FR,2)
    
    win.close()    # Close window when done

main()