from graphics import *
import numpy as np

def remove(obj):
    obj.setOutline("white")
    obj.setFill("white")
    
def wait(FR,sec):
    for i in range(FR*sec):
        update(FR)
        
def exp_lin(x,y,r0,er_lin,window,SL,SS,EX,FR):
    obj = Circle(Point(x,y), r0)
    obj.setFill("black")
    obj.draw(window)    
    for i in range(SL):
        if i<SS:
            obj.setFill("black")
        elif i<EX:
            r = obj.getRadius()
            obj = Circle(Point(x,y), r+er_lin)
            obj.setFill("black")
            obj.draw(window)    
        elif i<SL:
            obj.setFill("black")
        update(FR)
    return obj

def exp_exp(x,y,r0,er_exp,window,SL,SS,EX,FR,n):    
    obj = Circle(Point(x,y), r0)
    obj.setFill("black")
    obj.draw(window)    
    for i in range(SL):
        if i<SS:
            obj.setFill("black")
        elif i<EX:
            r = obj.getRadius()
            obj = Circle(Point(x,y), r0*np.exp(er_exp*(i-SS)**n))
            obj.setFill("black")
            obj.draw(window)    
        elif i<SL:
            obj.setFill("black")
        update(FR)
    return obj

def exp_sig(x,y,r0,rf_e,er_exp,window,SL,SS,EX,FR,n):
    obj = Circle(Point(x,y), r0)
    obj.setFill("black")
    obj.draw(window)    
    for i in range(SL):
        if i<SS:
            obj.setFill("black")
        elif i<EX:
            r = obj.getRadius()
            obj = Circle(Point(x,y), rf_e - rf_e*np.exp(-er_exp*(i-SS)**n))
            obj.setFill("black")
            obj.draw(window)    
        elif i<SL:
            obj.setFill("black")
        update(FR)
    return obj
    
def red_lin(x,y,rf_l,er_lin,window,SL,SS,EX,FR):
    obj = Circle(Point(x,y), rf_l)
    obj.setFill("black")
    obj.draw(window)    
    print('drawing shadow #5')
    for i in range(SL):
        if i<SS:
            obj.setFill("black")
        elif i<EX:
            r = obj.getRadius()
            obj_temp = Circle(Point(x,y), r - er_lin)
            obj_temp.setFill("black")
            obj_temp.draw(window)    
            obj.undraw()
            obj = obj_temp
        elif i<SL:
            obj.setFill("black")
        update(FR)
    return obj
    
def stable(x,y,r0,window,SL,FR):
    obj = Circle(Point(x,y), r0)
    obj.setFill("black")
    obj.draw(window)    
    for i in range(SL):
        obj.setFill("black")
        update(FR)
    return obj