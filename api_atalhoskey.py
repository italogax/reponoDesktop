from api_caixaReg import *

from keyboard import *

def keypress(event):
    if event.keysym == "1":
        sub_total()

    else: 
        keypress(event)