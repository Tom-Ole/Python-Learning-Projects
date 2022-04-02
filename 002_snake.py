import pygame
import time
import random

pygame.init()

display_width = 500
display_height = 500
frameRate = 10

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")


color_snake = (0, 255, 0)
color_food = (255, 0, 0)
color_bg = (255, 255, 255)


snake_size = 10

def snake(snake_size, snake_body): 
    for x in snake_body:
        pygame.draw.rect(display, color_snake, [x[0], x[1], snake_size, snake_size])

def game():
    gameOver = False

    snake_x = display_width/2
    snake_y = display_height/2

    snake_move_x = 0
    snake_move_y = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0

    while not gameOver:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_move_x = -snake_size
                    snake_move_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_move_x = snake_size
                    snake_move_y = 0
                elif event.key == pygame.K_DOWN:
                    snake_move_x = 0
                    snake_move_y = snake_size
                elif event.key == pygame.K_UP:
                    snake_move_x = 0
                    snake_move_y = -snake_size
            if event.type == pygame.MOUSEMOTION:
                snake_move_x = 0
                snake_move_y = 0

            if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
                gameOver = True

        snake_x += snake_move_x
        snake_y += snake_move_y
        display.fill(color_bg)
        pygame.draw.rect(display, color_food, [food_x, food_y, snake_size, snake_size])
        snake_body.append([snake_x, snake_y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == [snake_x, snake_y]:
                gameOver = True
        
        snake(snake_size, snake_body)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        pygame.time.Clock().tick(frameRate)

    pygame.quit()
    quit()
 

game()
