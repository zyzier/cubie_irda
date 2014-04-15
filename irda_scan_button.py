#encoding utf-8 
''' Скрипт для определения кода кавиши на пульте,
 записывающий код клавиши в файл '''

import string
from evdev import InputDevice
from select import select

#Файл устройтва
dev = InputDevice('/dev/input/event0')

#Бесконечный цикл проверки файла устройства на наличие кода нажатой клавиши
while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
        if event.type==1 and event.value==1:
                #при обнаружении кода запиывать его в файл
                open('/dev/irda', 'w').write(str(event.code))

