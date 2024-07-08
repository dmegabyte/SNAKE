import pygame
import sys

pygame.init()



CELL_SIZE = 60

class Snake:
    def __init__(self,x,y,width,height,color,RIGHT,LEFT,DOWN,UP):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.RIGHT = RIGHT
        self.LEFT = LEFT
        self.DOWN = DOWN
        self.UP = UP

    def Draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define some colors
BLUE = (0, 128, 255)

snake = Snake(x=160,y=160,width=CELL_SIZE,height=CELL_SIZE,color=BLUE,RIGHT=79,LEFT=80,DOWN=81,UP=82)


def screen_update():
    pygame.display.flip()
    pygame.time.Clock().tick(2)

def screen_draw():
    snake.Draw()

# Цикл игры
def game_loop():
    while True:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.scancode == snake.DOWN:
                    print(event.scancode)
                                   
        screen_draw()
        screen_update()
game_loop()