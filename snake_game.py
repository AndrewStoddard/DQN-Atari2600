import pygame, sys, time, random

width = 500
height = 500
speed = 20

pygame.init()

environment = pygame.display.set_mode((width, height))
fps_controller = pygame.time.Clock()

snake_position = [width / 2, height / 2]
snake_body = [[width / 2, height / 2], [(width / 2) - 10, height / 2], [(width / 2) - 20, height / 2]]

food_position = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
is_food_spawned = True

current_direction = 'RIGHT'
next_direction = current_direction

score = 0

def game_over():
    pygame.quit()
    sys.exit()
def transfer_snake(side): 
    if side == "LEFT": 
        snake_position[0] = 0
        for part_num in range(len(snake_body)):
            snake_body[part_num][0] = -(part_num * 10)
    elif side == "RIGHT":
        snake_position[0] = width
        for part_num in range(len(snake_body)):
            snake_body[part_num][0] = (part_num * 10) + width
    elif side == "TOP":
        snake_position[1] = height
        for part_num in range(len(snake_body)):
            snake_body[part_num][1] = (part_num * 10) + height
    elif side == "BOTTOM":
        snake_position[1] = 0
        for part_num in range(len(snake_body)):
            snake_body[part_num][1] = -(part_num * 10)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                next_direction = 'UP'
            if event.key == pygame.K_s:
                next_direction = 'DOWN'
            if event.key == pygame.K_a:
                next_direction = 'LEFT'
            if event.key == pygame.K_d:
                next_direction = 'RIGHT'

    if current_direction != 'UP' and next_direction == 'DOWN':
        current_direction = 'DOWN'
    if current_direction != 'DOWN' and next_direction == 'UP':
        current_direction = 'UP'
    if current_direction != 'LEFT' and next_direction == 'RIGHT':
        current_direction = 'RIGHT'
    if current_direction != 'RIGHT' and next_direction == 'LEFT':
        current_direction = 'LEFT'

    if current_direction == 'UP':
        snake_position[1] -= 10
    if current_direction == 'DOWN':
        snake_position[1] += 10
    if current_direction == 'LEFT':
        snake_position[0] -= 10
    if current_direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        speed += .25
        is_food_spawned = False
    else:
        snake_body.pop()

    if not is_food_spawned:
        food_position = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        is_food_spawned = True
    if snake_position[0] < 0:
        transfer_snake("RIGHT")
    elif snake_position[0] > width:
        transfer_snake("LEFT")
    elif snake_position[1] < 0:
        transfer_snake("TOP")
    elif snake_position[1] > height:
        transfer_snake("BOTTOM")



    environment.fill(pygame.Color(60, 60, 60))
    for part in snake_body:
        pygame.draw.rect(environment, pygame.Color(0, 255, 0), pygame.Rect(part[0], part[1], 10, 10))
    
    pygame.draw.rect(environment, pygame.Color(255, 255, 255), pygame.Rect(food_position[0], food_position[1], 10, 10))

    pygame.display.update()
    fps_controller.tick(speed)