# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

#init GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup()
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up


def readGPIO(draw):
    # with canvas(device) as draw:
    c="orange"
    o="orange"
    #UP
    position=[(75, 20), (80, 9), (85, 20)]
    if GPIO.input(KEY_UP_PIN) == 0: # button is released       
        draw.polygon(position, outline=o, fill=c)  #Up        
        return ("Up")        
    else: # button is pressed:
        draw.polygon(position, outline=o, fill=0)  #Up filled
     #LEFT  
    position=[(75, 20), (64, 26), (75, 32)] 
    if GPIO.input(KEY_LEFT_PIN) == 0: # button is released
        draw.polygon(position, outline=o, fill=c)  #left
        return("left")        
    else: # button is pressed:       
        draw.polygon(position, outline=o, fill=0)  #left filled
    #RIGHT
    position=[(85, 20), (96, 26), (85, 32)]  
    if GPIO.input(KEY_RIGHT_PIN) == 0: # button is released
        draw.polygon(position, outline=o, fill=c) #right
        return("right")
    else: # button is pressed:
        draw.polygon(position, outline=o, fill=0) #right filled   
    #DOWN   
    position=[(75, 32), (80, 43), (85, 32)]    
    if GPIO.input(KEY_DOWN_PIN) == 0: # button is released
        draw.polygon(position, outline=o, fill=c) #down
        return("down")
    else: # button is pressed:
        draw.polygon(position, outline=o, fill=0) #down filled
    #RECTANGLE BUTTON
    position=(75,20,85,32)
    if GPIO.input(KEY_PRESS_PIN) == 0: # button is released
        draw.rectangle(position, outline=o, fill=c) #center 
        return("center")
    else: # button is pressed:
        draw.rectangle(position, outline=o, fill=0) #center filled
    #BTN1
    c="green"
    position=[100,10,110,20]
    if GPIO.input(KEY1_PIN) == 0: # button is released
        draw.ellipse(position, outline=c, fill=c) #A button
        return("KEY1")
    else: # button is pressed:
        draw.ellipse(position, outline=c, fill=0) #A button filled
    #BTN2
    c="red"
    position=[110,20,120,30]  
    if GPIO.input(KEY2_PIN) == 0: # button is released
        draw.ellipse(position, outline=c, fill=c) #B button]
        return("KEY2")
    else: # button is pressed:
        draw.ellipse(position, outline=c, fill=0) #B button filled
    #BTN3   
    c="blue"
    position=[100,30,110,40]
    if GPIO.input(KEY3_PIN) == 0: # button is released
        draw.ellipse(position, outline=c, fill=c) #A button
        return("KEY3")
    else: # button is pressed:
        draw.ellipse(position, outline=c, fill=0) #A button filled
# except:
	# print("except")
    # GPIO.cleanup()
