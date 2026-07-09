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
ORANGE = (255, 170, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

socket_on = True
generator = False

battery = 100

button = pygame.Rect(520, 20, 250, 50)

socket = (100, 180)
battery_pos = (100, 350)
server = (600, 250)

points = []

for i in range(20):
    points.append(i * 0.05)

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                socket_on = not socket_on

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                generator = not generator

    # Разряд батареи
    if not socket_on and not generator:
        battery -= 10 * dt

    if battery < 0:
        battery = 0

    # Конец игры
    if battery == 0 and not generator:
        screen.fill(BLACK)
        txt = pygame.font.SysFont(None, 50).render(
            "СЕРВЕР ВЫКЛЮЧЕН", True, RED)
        screen.blit(txt, (220, 220))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    screen.fill(WHITE)

    # Розетка
    pygame.draw.rect(screen, BLUE, (70, 150, 60, 60))

    # Батарея
    pygame.draw.rect(screen, GRAY, (60, 330, 90, 40))

    # Сервер
    pygame.draw.rect(screen, GREEN, (560, 220, 80, 60))

    # Провода
    pygame.draw.line(screen, BLACK, socket, server, 4)
    pygame.draw.line(screen, BLACK, battery_pos, server, 4)

    # Кнопка
    pygame.draw.rect(screen, RED, button)

    if socket_on:
        text = "Отключить питание"
    else:
        text = "Включить питание"

    screen.blit(font.render(text, True, WHITE), (540, 35))

    # Статусы
    if socket_on:
        status = "Питание: ВКЛ"
        color = GREEN
    else:
        status = "Питание: ВЫКЛ"
        color = RED

    screen.blit(font.render(status, True, color), (20, 20))

    if generator:
        gen = "Генератор: ВКЛ (G)"
        gen_color = GREEN
    else:
        gen = "Генератор: ВЫКЛ (G)"
        gen_color = RED

    screen.blit(font.render(gen, True, gen_color), (20, 55))

    # Шкала батареи
    pygame.draw.rect(screen, BLACK, (20, 95, 200, 25), 2)

    if battery > 60:
        bar_color = GREEN
    elif battery > 30:
        bar_color = ORANGE
    else:
        bar_color = RED

    pygame.draw.rect(screen, bar_color, (20, 95, battery * 2, 25))

    screen.blit(font.render(f"{int(battery)}%", True, BLACK), (230, 95))

    # Частицы
    for i in range(len(points)):

        points[i] += 0.01

        if points[i] > 1:
            points[i] = 0

        t = points[i]

        if socket_on:
            start = socket
        else:
            start = battery_pos

        x = start[0] + (server[0] - start[0]) * t
        y = start[1] + (server[1] - start[1]) * t

        pygame.draw.circle(screen, ORANGE, (int(x), int(y)), 4)

    pygame.display.flip()

pygame.quit()