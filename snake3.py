import pygame
import sys
import random

clock = pygame.time.Clock()
pygame.init()

move = 'go down'

options = {
    'FPS': 3,
    'WIDTH': 1000,
    'HEIGHT': 1000,
    'GREEN': (0, 255, 0),
    'SCORE': 0,
}

keyscancode = {
    'UP': 82,
    'DOWN': 81,
    'LEFT': 80,
    'RIGHT': 79, 
}
screen = pygame.display.set_mode((options['WIDTH'], options['HEIGHT']))
snake = [[0, 0],[0, 0]]


def game_over():          
    for x,y in snake:
        if (x >= 1000 or y >= 1000) or (x < 0 or y < 0) or (len(snake)!= len(frozenset(map(tuple, snake)))):
            screen_gameover(options)       
        else:
            return options['FPS']  

def move_function(head,move):
    if move == 'go up':
        head[1] -= 50
    elif move == 'go down':
        head[1] += 50
    elif move == 'go left':
        head[0] -= 50
    elif move == 'go right':
        head[0] += 50
    else:
        pass
    return head
    
def random_num():
    random_number = random.randint(0, 19) * 50
    return random_number

def draw_snake(snake):       
    for x, y in snake:
        pygame.draw.rect(screen, options['GREEN'], (x, y, 50, 50))
def snake_move(snake,move):
    head = snake[0].copy()
    snake_copy = snake.copy()  
    for i in range(len(snake)):
        if i ==0:
            move_function(head,move)
        elif i >0:               
            snake[i] = snake_copy[i-1].copy()
    snake[0] = head.copy()
    # print(snake)

def screen_gameover(options):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 150)
        text_message = font.render(f'Game over', True, (255, 255, 255))
        text_score = font.render(f'Score {options['SCORE']}', True, (255, 255, 255))
        screen.blit(text_message, (210, 300))
        screen.blit(text_score, (300, 500))
    
        pygame.display.flip()   
def keydown(event,move):
    if event.scancode == keyscancode['UP'] and move != 'go down':
        return 'go up'
    elif event.scancode == keyscancode['DOWN'] and move != 'go up':
        return 'go down'
    elif event.scancode == keyscancode['LEFT'] and move != 'go right':
        return 'go left'
    elif event.scancode == keyscancode['RIGHT'] and move != 'go left':
        return 'go right'
    else:
        return move  
def create_food():
    food = [(random_num()),(random_num())]
    while food == snake[0]:
        food = [random_num(), random_num()]
    return food    
food = create_food()        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            move = keydown(event,move)
    if food:
        pygame.draw.rect(screen, options['GREEN'], (food[0], food[1], 50, 50))
    else:
        pass
    
    
    
#проверка столкновений
    if food == snake[0]:
        print(food,snake[0])
        snake.append(food)
        food = create_food()
        options['FPS'] +=1
        options['SCORE'] += 1
                    
            

    font = pygame.font.Font(None, 50)
    text = font.render(F"score {options['SCORE']}", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    snake_move(snake,move)
    options['FPS'] = game_over()
    draw_snake(snake)

    pygame.display.flip()                          
    
    clock.tick(options['FPS'])
    screen.fill((0, 0, 0))
