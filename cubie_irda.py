#encoding utf-8
''' Main script for cubie remote control
    For now it using for manage mpd server '''
import string
import os

from evdev import InputDevice
from select import select

#Device file
dev = InputDevice('/dev/input/event0')

def scan(device):
  '''Infinity loop that checks the device file'''
    while True:
       r,w,x = select([device], [], [])
       for event in device.read():
           if event.type==1 and event.value==1:
               if str(event.code) == "66":
                   os.system("mpc prev")
               elif str(event.code) == "67":
                   os.system("mpc next")
               elif str(event.code) == "32":
                   os.system("amixer set Master playback 2%+")
               elif str(event.code) == "33":
                   os.system("amixer set Master playback 2%-")

scan(dev)
