import pygame       # importing pygame
import random       # importing random for generating random values
import os           # importing os for generating file if not exists

# initializing pygame
pygame.init()

# initializing mixer for playing sounds or music
pygame.mixer.init()

# saving screen width and height in variables
screen_width = 900
screen_height = 600

# rgb colors
white = (255, 255, 255)
red = (255, 0, 0)
orange = (222, 128, 78)
purple = (150, 70, 255)
black = (0, 0, 0)
blue = (20, 140, 250)
lightGreen = (196, 228, 157)
brown = (59, 58, 62)

# setting the fps: frames per second
fps = 60

# generating game window and caption
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()  # for updating everytime

# saving and loading images
bg_img = pygame.image.load("bg-img.jpg")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()

snake_img = pygame.image.load("snake.jpg")
snake_img = pygame.transform.scale(snake_img, (screen_width, screen_height)).convert_alpha()

over_img = pygame.image.load("over.jpg")
over_img = pygame.transform.scale(over_img, (screen_width, screen_height)).convert_alpha()

# setting clock
clock = pygame.time.Clock()
# setting font
font = pygame.font.SysFont(str(None), 60)


# defining functions for text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])


def over_screen(text, color, x, y):
    over_text = font.render(text, True, color)
    game_window.blit(over_text, [x, y])


def plot_snake(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])


# defining loops
# welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        # game_window.fill(blue)
        game_window.blit(snake_img, (0, 0))
        text_screen("Welcome to Snakes", lightGreen, screen_width / 3.8, 50)
        over_screen("Press ENTER to Continue", lightGreen, screen_width / 5, 540)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    game_loop()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        pygame.display.update()
        clock.tick(fps)


def game_loop():
    score = 0
    if not os.path.exists("hi_score.txt"):
        with open("hi_score.txt", "w") as f:
            f.write(str(0))
    with open("hi_score.txt", "r") as f:
        hi_score = f.read()
    snake_x = 45
    snake_y = 55
    snake_size = 30
    food_size = 10
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, int(screen_width))
    food_y = random.randint(20, int(screen_height))
    snk_list = []
    snk_length = 1
    game_over = False
    exit_game = False

    while not exit_game:
        if game_over:
            with open("hi_score.txt", "w") as f:
                f.write(str(hi_score))
            # game_window.fill(brown)
            game_window.blit(over_img, (0, 0))
            over_screen("GAME OVER!!!", blue, 290, 320)
            over_screen("Press ENTER to Continue", blue, screen_width / 5, 540)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # game_loop()
                        welcome()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

        else:
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

                    if event.key == pygame.K_SPACE:
                        score += 10
                    elif event.key == pygame.K_TAB:
                        score -= 10

                    if event.key == pygame.K_F1:
                        init_velocity += 3
                    elif event.key == pygame.K_F12:
                        init_velocity -= 3

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit()

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18:
                score += 10
                food_x = random.randint(20, int(screen_width))
                food_y = random.randint(20, int(screen_height))
                snk_length += 5
            if score > int(hi_score):
                hi_score = score

            # game_window.fill(white)
            game_window.blit(bg_img, (0, 0))
            text_screen("Score: " + str(score) + "  HiScore: " + str(hi_score), purple, 5, 5)
            pygame.draw.circle(game_window, red, [food_x, food_y], food_size, food_size)

            head = list()
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()
                game_over = True

            plot_snake(game_window, orange, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
