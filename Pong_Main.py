import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Pong")

bg = pygame.image.load("assets/field.png")
window.blit(bg, (0, 0))

loop = True
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()       