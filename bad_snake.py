import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
options = {
    'CELL_SIZE': 60,
    'CELL_COLOR': (0,128,255),
    'FIRST_POSITION_X': 0,
    'FIRST_POSITION_Y': 0,
}
keyscancode = {
    'UP': pygame.K_UP,
    'DOWN': pygame.K_DOWN,
    'LEFT': pygame.K_LEFT,
    'RIGHT': pygame.K_RIGHT, 
}

x_s = 0
y_s = 0
snake_list = [[x_s, y_s]]
snake_map = [[0 for y in range(10)] for x in range( 10)]
snake_map[x_s][y_s] = 60

def snakeFunc():
    for x in range(len(snake_map)):
        for y in range(len(snake_map[x])):
            if snake_map[x][y] == 60:
                return x, y
    return 0, 0

snake_position = snakeFunc()

def keydown(event):
    if event.key == keyscancode['UP']:
        return 'go up'
    elif event.key == keyscancode['DOWN']:
        return 'go down'
    elif event.key == keyscancode['LEFT']:
        return 'go left'
    elif event.key == keyscancode['RIGHT']:
        return 'go right'

clock = pygame.time.Clock()

def game_loop():
    x = options['FIRST_POSITION_X']
    y = options['FIRST_POSITION_Y']
    hight = options['CELL_SIZE']
    width = options['CELL_SIZE']
    move = 'go right'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                move = keydown(event)
        if move == 'go right':
            x = (x + options['CELL_SIZE']) % 900
            snake_list.append([x, y])
        elif move == 'go left':
            x = (x - options['CELL_SIZE']) % 900
            snake_list.append([x, y])
        elif move == 'go down':
            y = (y + options['CELL_SIZE']) % 900
            snake_list.append([x, y])
        elif move == 'go up':
            y = (y - options['CELL_SIZE']) % 900
            snake_list.append([x, y])

        screen.fill((0, 0, 0))  # Очистка экрана

        for pos in snake_list:
            pygame.draw.rect(screen, options['CELL_COLOR'], pygame.Rect(pos[0], pos[1], width, hight))

        pygame.display.flip()
        clock.tick(10)

game_loop()