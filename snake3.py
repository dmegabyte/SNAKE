import pygame
import sys
import random

clock = pygame.time.Clock()
pygame.init()

move_list = ['go down','go right']

move = ' '

class Options:
    fps = 3
    WIDTH = 800
    HEIGHT = 700
    size = 50
    score = 0

class Game():
    def __init__(self):
        self.score = 0


class Color:
    red = (255, 0, 0)
    green = (0, 255, 0)

game = Game()

keyscancode = {
    'UP': 82,
    'DOWN': 81,
    'LEFT': 80,
    'RIGHT': 79, 
}
screen = pygame.display.set_mode((Options.WIDTH, Options.HEIGHT))
snake = [[0, 0],[0, 0]]


def game_over():          
    for x,y in snake:
        if (x >= Options.WIDTH or y >= Options.HEIGHT ) or (x < 0 or y < 0) :
            screen_gameover(Options)
        for i in range(2,len(snake)):
            if snake[0] == snake[i]:
                screen_gameover(Options)     
        else:
            return Options.fps 

def move_function(head,move):
    if move == 'go up':
        head[1] -= Options.size
    elif move == 'go down':
        head[1] += Options.size
    elif move == 'go left':
        head[0] -= Options.size
    elif move == 'go right':
        head[0] += Options.size
    else:
        pass
    return head
    
def random_num():
    random_x = random.randint(0, int(Options.WIDTH/Options.size - 1)) * Options.size
    random_y = random.randint(0,  int(Options.HEIGHT/Options.size - 1)) * Options.size
    return [random_x,random_y]

def draw_snake(snake):       
    for x, y in snake:
        pygame.draw.rect(screen, Color.green, (x, y, Options.size, Options.size))
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
        text_size = 80
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, text_size)
        text_message = font.render(f'Game over', True, (255, 255, 255))
        text_score = font.render(f'Score {Options.score}', True, (255, 255, 255))
        text_rect = text_message.get_rect(center=(Options.WIDTH/2, Options.HEIGHT/2-100))
        screen.blit(text_message, text_rect)

        text_rect = text_score.get_rect(center=(Options.WIDTH/2, Options.HEIGHT/2 + text_size))
        screen.blit(text_score, text_rect)
    
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
    food = random_num()
    while food == snake[0]:
        food = random_num()
    return food    
food = create_food()        
while True:
    u = True
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and u:
            u = False
            move = keydown(event,move)

    

#проверка столкновений
    if food == snake[0]:
        print(food,snake[0])
        snake.append(food)
        food = create_food()
        Options.fps+=1
        Options.score += 1
                             
    font = pygame.font.Font(None, 50)
    text = font.render(F"score {Options.score}", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    snake_move(snake,move)
    Options.fps = game_over()

    pygame.draw.rect(screen, Color.red, (food[0]+Options.size*0.2, food[1]+Options.size*0.2, Options.size*0.6, Options.size*0.6))
    draw_snake(snake)

    pygame.display.flip()                          
    
    clock.tick(Options.fps)
    screen.fill((0, 0, 0))
