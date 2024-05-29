import pygame
import random
#музика
pygame.mixer.init()
pygame.mixer.music.load("pixel.mp3")
pygame.mixer.music.play()
# Ініціалізація Pygame
pygame.init()

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Розміри блоків та швидкість руху змійки
BLOCK_SIZE = 20
SPEED = 10  # Половина швидкості руху змійки

# Ініціалізація вікна гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Функція виведення тексту
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Функція головного меню
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text('Змійка', pygame.font.Font(None, 100), GREEN, screen, 300, 150)
        draw_text('Нажміть любу клавішу', pygame.font.Font(None, 50), WHITE, screen, 210, 300)
        draw_text('Нажміть ESC щоб вийти', pygame.font.Font(None, 50), WHITE, screen, 200, 400)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    return

# Функція виведення змійки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Основна функція гри
def game_loop():
    # Початкові координати змійки
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Початкова довжина змійки та шлях її руху
    snake_list = []
    snake_length = 1

    # Початкові координати миші
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    # Початкова швидкість змійки
    x_change = 0
    y_change = 0

    # Рахунок очків
    score = 0

    # Основний цикл гри
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Зміна координат змійки
        x += x_change
        y += y_change

        # Перевірка, чи змійка зіткнулася з межами екрану
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Перевірка, чи змійка з'їла їжу
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Оновлення рахунку
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            snake_length += 1
            score += 1

        # Виведення змійки та рахунку
        draw_snake(BLOCK_SIZE, snake_list)
        draw_text("Score: {}".format(score), pygame.font.Font(None, 30), WHITE, screen, 10, 10)
        pygame.display.update()

        # Встановлення частоти оновлення екрану
        pygame.time.Clock().tick(SPEED)

    # Виведення повідомлення про кінець гри
    draw_text("Game Over! Score: {}".format(score), pygame.font.Font(None, 70), RED, screen, 150, 250)
    pygame.display.update()
    pygame.time.delay(2000)

# Запуск головного меню та гри
main_menu()
game_loop()
pygame.quit()
quit()
