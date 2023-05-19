
import pygame
from random import randint
import time

clock = pygame.time.Clock()

pygame.init()

width = 1366
height = 768

icon = pygame.image.load("board1.png")

GD = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Snake and Ladders")
pygame.display.set_icon(icon)
pygame.display.update()

black = (10, 10, 10)
white = (250, 250, 250)
red = (200, 0, 0)
b_red = (240, 0 ,0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (150, 150, 0)
purple = (43, 3, 132)
b_purple = (60, 0, 190)

board = pygame.image.load("board1.jpg")
dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")
dice6 = pygame.image.load("dice6.png")

redgoti = pygame.image.load("redgoti.png")
yellowgoti = pygame.image.load("yellowgoti.png")
greengoti = pygame.image.load("greengoti.png")
bluegoti = pygame.image.load("bluegoti.png")
menubg = pygame.image.load("menu.jpg")
p = pygame.image.load("playbg.jpg")

intbg = pygame.image.load("intropic.jpg")
intbg2 = pygame.image.load("intropic2.jpg")
intbg3 = pygame.image.load("intropic3.jpg")
intbg4 = pygame.image.load("intropic4.jpg")
intbg5 = pygame.image.load("intropic5.jpg")















