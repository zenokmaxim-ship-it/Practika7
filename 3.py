import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Система бесперебойного питания")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 180, 0)
GRAY = (130, 130, 130)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)

clock = pygame.time.Clock()

# Питание включено
socket_on = True

button = pygame.Rect(520, 20, 250, 50)

socket = (100, 180)
server = (600, 250)
battery = (100, 350)

points = []
for i in range(20):
    points.append(i * 0.05)

font = pygame.font.SysFont(None, 28)

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # Переключаем питание
                socket_on = not socket_on

    screen.fill(WHITE)

    # Розетка
    pygame.draw.rect(screen, BLUE, (70, 150, 60, 60))

    # Батарея
    pygame.draw.rect(screen, GRAY, (60, 330, 90, 40))

    # Сервер
    pygame.draw.rect(screen, GREEN, (560, 220, 80, 60))

    # Провода
    pygame.draw.line(screen, BLACK, socket, server, 4)
    pygame.draw.line(screen, BLACK, battery, server, 4)

    # Кнопка
    pygame.draw.rect(screen, RED, button)

    if socket_on:
        text = "Отключить питание"
    else:
        text = "Включить питание"

    screen.blit(font.render(text, True, WHITE), (540, 35))

    # Статус
    if socket_on:
        status = font.render("Питание: ВКЛ", True, GREEN)
    else:
        status = font.render("Питание: ВЫКЛ", True, RED)

    screen.blit(status, (20, 20))

    # Частицы тока
    if socket_on:
        for i in range(len(points)):

            points[i] += 0.01
            if points[i] > 1:
                points[i] = 0

            t = points[i]

            x = socket[0] + (server[0] - socket[0]) * t
            y = socket[1] + (server[1] - socket[1]) * t

            pygame.draw.circle(screen, ORANGE, (int(x), int(y)), 4)

    pygame.display.flip()

pygame.quit()