#coding:utf-8
import sys
import pygame
pygame.init()
pygame.display.set_caption("PygameApplication")
canvas=pygame.display.set_mode((500,300))
bg=pygame.image.load("images/background.png")
def display():
    canvas.blit(bg,(0,0))
while True:
    display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    

