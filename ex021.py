#3 formas de tocar um mp3 no Pycharm


import pygame
pygame.mixer.init()
pygame.mixer.music.load('desafio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#from playsound import playsound
#playsound('desafio.mp3')

#import os
#os.system('desafio.mp3')



