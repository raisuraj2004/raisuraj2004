import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 5
snake_speed = 10

font = pygame.font.SysFont(None, 25)

def message(msg, color):
    mesg = font.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width/3, display_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1_change = 0
    y1_change = 0

    x1_start = display_width/2
    y1_start = display_height/2

    x1_snake = x1_start
    y1_snake = y1_start

    snake_List = []
    Length_of_snake = 1

    randAppleX = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            gameDisplay.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1_snake >= display_width or x1_snake < 0 or y1_snake >= display_height or y1_snake < 0:
            game_close = True

        x1_snake += x1_change
        y1_snake += y1_change

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1_snake)
        snake_Head.append(y1_snake)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)

        pygame.display.update()

        if x1_snake == randAppleX and y1_snake == randAppleY:
            randAppleX = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, blue, [x[0], x[1], snake_block, snake_block])

gameLoop()