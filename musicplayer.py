import serial
import pygame

import pygame
pygame.mixer.init()


ser serial.Serial('/dev/ttyACM0', 9600)

isPlaying = False

def playMusic(tone):
	s = new Sound()
	s.read(tone..)
	pygame.mixer.music.load("myFile.wav")
	pygame.mixer.music.play()
	isPlaying = True
	while pygame.mixer.music.get_busy() == True:
    continue
return;


# Read serial
while True : 
	inp = ser.readline()
	if( inp.)
