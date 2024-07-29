import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Pong")

field = pygame.image.load("assets/field.png")
window.blit(field, (0, 0))

player1 = pygame.image.load("assets/player1.png")
window.blit(player1, (50, 310))

player2 = pygame.image.load("assets/player2.png")
window.blit(player2, (1150, 310))

ball = pygame.image.load("assets/ball.png")
window.blit(ball, (617, 337))

loop = True
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()       