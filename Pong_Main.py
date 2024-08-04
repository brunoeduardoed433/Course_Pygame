import pygame


pygame.init()


window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Pong")


field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

def move_player():

    global player1_y
    global player2_y

 #Player 1

    if player1_moveup:

        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:

        player1_y += 5
    else:
        player1_y += 0    

 #Player 2

    if player2_moveup:

        player2_y -= 5
    else:
        player2_y += 0

    if player2_movedown:

        player2_y += 5
    else:
        player2_y += 0
        
    #Limitação Player 1
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

    #Limitação Player 2
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575


player2 = pygame.image.load("assets/player2.png")
player2_y = 310
player2_moveup = False
player2_movedown = False

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = 5
ball_dir_y = 1

# Movimentação da Bolinha
def move_ball():

    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1 
    
    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1



def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, player2_y))
    window.blit(ball, (ball_x, ball_y))


loop = True
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            else:
                if events.key == pygame.K_s:
                    player1_movedown = True
                else:
                    if events.key ==  pygame.K_UP:
                        player2_moveup = True
                    else:
                        if events.key == pygame.K_DOWN:
                            player2_movedown = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            else:
                if events.key == pygame.K_s:
                    player1_movedown = False
                else:
                    if events.key ==  pygame.K_UP:
                        player2_moveup = False
                    else:
                        if events.key == pygame.K_DOWN:
                            player2_movedown = False

    draw()
    move_ball()
    move_player()
    pygame.display.update()       