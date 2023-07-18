from tkinter import *
import random
import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
# getting info
info = pygame.display.Info()
# setting screen width and height
WIDTH, HEIGHT = info.current_w, info.current_h
print(WIDTH, HEIGHT)
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0080"
BACKGROUND_COLOR = "#000000"
WHITE = "#FFFFFF"
LIME = "#00FF00"
class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snek Game")
window.resizable(True, True)

score = 0
direction = "down"

label = Label(window, text = "Score:{}".format(score), font=("cursive", 40),  fg=LIME)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.mainloop()