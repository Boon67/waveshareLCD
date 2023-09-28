import LCD_1in44
import LCD_Config
from threading import Thread
import socket, time
from datetime import datetime
import gpio_inputs

LOGOFILE="logo.png"

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

from PIL import Image,ImageDraw,ImageFont,ImageColor
def getLCD():
    LCD = LCD_1in44.LCD()
    print ("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    return LCD

import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
def clock(draw):
    while True:
        LCD=getLCD()
        now= datetime.now()
        current_time=now.strftime("%H:%M:%S")
        draw.text((10, 10), current_time, fill = "WHITE")
        print(current_time)
        LCD.LCD_ShowImage(image,0,0)
        time.sleep(1)
        
def main():
#try:
    LCD=getLCD()
    LCD.LCD_Clear()
    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    fg_image = Image.open(LOGOFILE)
    fg_image = fg_image.resize((120,32), Image.ANTIALIAS)
    image.paste(fg_image,(4,48), fg_image)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
    print ("***draw outline")
    draw.line([(0,0),(127,0)], fill = "WHITE",width = 1)
    draw.line([(127,0),(127,127)], fill = "WHITE",width = 1)
    draw.line([(127,127),(0,127)], fill = "WHITE",width = 1)
    draw.line([(0,127),(0,0)], fill = "WHITE",width = 1)
    lastButton=None
    while True:
        LCD.LCD_ShowImage(image,0,0)
        now = datetime.now()
        current_time=now.strftime("%H:%M:%S")
        draw.rectangle([(10,10),(80,20)],fill = "BLACK")
        draw.text((10, 10), current_time, fill = "WHITE")
        draw.text((10, 100), 'Host:' + hostname, fill = "GREEN")
        draw.text((10, 110), 'IP: ' + get_ip(), fill = "BLUE")
        #Need to make this be interrupt driven
        result=gpio_inputs.readGPIO(draw)
        if lastButton!=result:
            print(result)
            lastButton=result
        LCD.LCD_ShowImage(image,0,0)
        LCD_Config.Driver_Delay_ms(0)
        time.sleep(.1)
	
if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()





