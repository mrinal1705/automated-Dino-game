import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # for birds
    for i in range(300, 415):
        for j in range(550, 587):
            if data[i, j] < 100:
                hit("down")
                hit("down")
                print('duck')
                return

    #for Cactus
    for i in range(250, 630):
        for j in range(690, 695):
            if data[i, j] < 100:
                hit("up")
                print('jump')
                return


    return


if __name__ == '__main__':
    print("Dino game is about to start in 3 seconds")
    time.sleep(2)
    hit('up')
    #hit('down')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


        #print(asarray(image))

        '''

        for i in range(250, 650):
            for j in range(690, 695):
                data[i, j] =  0


        # for birds
        for i in range(250, 650):
            for j in range(550, 587):
                data[i, j] = 171

                print('duck')


        image.show()
        break
        
        '''





