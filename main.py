# Fabien Thich & Dillan Do
# January 9, 2023

import pygame, sys
from pygame.locals import QUIT
import random
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
ORANGE = (255,165,0)
PURPLE = (230,230,250)

def gameStart():
  
    COLOUR_LIST = ["BLACK","WHITE", "RED", "YELLOW", "BLUE", "ORANGE", "PURPLE"]
    gen_list = []
    
    stillPlaying = True  
    
    while stillPlaying == True: 
      EASY = 3
      MEDIUM = 4
      HARD = 5
      print("----------------------TEST YOUR MEMORY!----------------------")
      mode = input("Enter difficulty (easy, medium, hard): ")
      print("\n")
      if mode.upper() == "EASY":
        mode = EASY
      elif mode.upper() == "MEDIUM":
        mode = MEDIUM
      else:
        mode = HARD
      for i in range(mode):  
        screen_colour = COLOUR_LIST[random.randint(0,mode)]  
        if i != 0:
         while screen_colour == gen_list[i - 1]:
            screen_colour = COLOUR_LIST[random.randint(0,mode)] 
        gen_list.append(screen_colour)  
        
      pygame.init()  
      screen = pygame.display.set_mode((700, 400))  
      pygame.display.set_caption('Is your right sided brain healthy?')  
    
      screen.fill(COLOUR_LIST[6]) 
      font = pygame.font.SysFont('Calibri', 25, True, False)
      text = font.render("Start!",True,BLACK)
      screen.blit(text, [250, 150])
      pygame.display.update()
      time.sleep(1)
      for i in range(mode):
        screen.fill(gen_list[i])
        time.sleep(1)
        pygame.display.update()  
    
      user_guess = input("What was the order? (seperated by spaces) **Purple does not count:**\n")
      user_guess = user_guess.upper()  
      user_guess = user_guess.split()          
      
      if user_guess == gen_list:
        print("\nYou won!")
        replay = input("\nDo you want to keep going? (Type Y to keep going): ")
        print("\n")
        if replay.upper() == "Y":
          gameStart()
          gen_list = []
        else:
          stillPlaying = False
          break
      else:
        print("\nOh no! You were wrong! The correct answer was: \n", '\n '.join(gen_list).lower())
        replay = input("\nDo you want to try again? (Type Y to try again) ")
        print("\n")
        if replay.upper() == "Y":
          gameStart()
          gen_list = []
        else:
          stillPlaying = False
          break
          
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:        
          pygame.quit()
          sys.exit()
        pygame.display.update()
        pygame.display.flip()

gameStart() 
