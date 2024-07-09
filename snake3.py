import pygame
import sys
import random

clock = pygame.time.Clock()
pygame.init()

move_list = ['go down','go right']

move = ' '
image_apple = pygame.image.load('images/apple50.png')
image_head = pygame.image.load('images/head_mini.png')
image_body = pygame.image.load('images/body7.png')
image_bad_apple = pygame.image.load('images/bad_apple.png')

class MySprite(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect()
        
    def rotate(self, angle):
        rotated_image = pygame.transform.rotate(self.original_image.copy(), angle)
        self.image = rotated_image
        self.rect = self.image.get_rect()

apple = MySprite(image_apple)
snake_head = MySprite(image_head)
snake_body = MySprite(image_body)

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


def image_rotate():
    
    if u != True:
        if move == 'go up':
            snake_head.rotate(180)

        elif move == 'go down':
            snake_head.rotate(0)

        elif move == 'go left':
            snake_head.rotate(-90)

        elif move == 'go right':
            snake_head.rotate(90)

        else:
            pass
        



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


def draw_objects():
    apple.rect.x = food[0]
    apple.rect.y = food[1]
    image_rotate()
     
    
    for i in snake:
        if i == snake[0]:
            snake_head.rect.x = snake[0][0]
            snake_head.rect.y = snake[0][1]
        else:
            snake_body.rect.x = i[0]
            snake_body.rect.y = i[1]
            screen.blit(snake_body.image,snake_body.rect)
    
    screen.blit(apple.image,apple.rect)
    screen.blit(snake_head.image,snake_head.rect)
    

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
        Options.fps+=0.1
        Options.score += 1
                             
    font = pygame.font.Font(None, 50)
    text = font.render(F"score {Options.score}", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    snake_move(snake,move)
    Options.fps = game_over()

    pygame.draw.rect(screen, Color.red, (food[0]+Options.size*0.2, food[1]+Options.size*0.2, Options.size*0.6, Options.size*0.6))
    
    

    draw_objects()
    # draw_snake(snake)
    pygame.display.flip()                          
    
    clock.tick(Options.fps)
    screen.fill((0, 0, 0))
