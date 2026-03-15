import pygame
import random

pygame.mixer.init()
filenames = ["Enregistrement.mp3","Enregistrement_2.mp3","Enregistrement_3.mp3",
             "Enregistrement_4.mp3","Enregistrement_5.mp3","Enregistrement_6.mp3","Enregistrement_7.mp3",
             "Enregistrement_8.mp3","Enregistrement_9.mp3","Enregistrement_10.mp3","Enregistrement_11.mp3",
             "Enregistrement_12.mp3","Enregistrement_13.mp3","Enregistrement_14.mp3","Enregistrement_15.mp3",
             "Enregistrement-16.mp3"]

sounds = [pygame.mixer.Sound(f) for f in filenames]

x=int(input("give me how much time it would take:"))

playy=[]

while(x>0):
    i = random.randint(0,15)
    print("added "+filenames[i])
    playy.append(sounds[i])
    x-=1

print("playing...")

# 'action' is now a pointer to the hardware channel
for i in range(len(playy)):  
    action = playy[i].play() 
    # You are asking the 'action' pointer: "Are you still busy?"
    while action.get_busy(): pygame.time.delay(10)
