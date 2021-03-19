import pygame
import random

pygame.init()

score = 0

screen_width = 900
screen_height = 600
snake_x = 45
snake_y = 55
snake_size = 30
food_size = 10

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

velocity_x = 0
velocity_y = 0
init_velocity = 5
fps = 60

food_x = random.randint(20, int(screen_width))
food_y = random.randint(20, int(screen_height))

game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE GAME")
Icon = pygame.image.load('icon.png')
pygame.display.set_icon(Icon)
pygame.display.update()

game_over = False
exit_game = False

clock = pygame.time.Clock()
font = pygame.font.SysFont(str(None), 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])
        # print([x, y])

snk_list = []
snk_length = 1

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18:
        score += 1
        # print("Score: ", score * 10)
        food_x = random.randint(20, int(screen_width))
        food_y = random.randint(20, int(screen_height))
        snk_length += 5

    game_window.fill(white)
    text_screen("Score: " + str(score * 10), blue, 5, 5)
    pygame.draw.circle(game_window, red, [food_x, food_y], food_size, food_size)

    head = list()
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    # pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
    plot_snake(game_window, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
