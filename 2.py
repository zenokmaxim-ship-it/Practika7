import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PowerSystem")

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,180,0)
GRAY = (150,150,150)

class PowerSystem:

    def __init__(self):
        self.server = pygame.Rect(500,170,120,120)
        self.socket = pygame.Rect(80,180,80,80)
        self.battery = pygame.Rect(80,320,120,50)

    def draw(self, screen):

        screen.fill(WHITE)

        pygame.draw.rect(screen, GREEN, self.server)
        pygame.draw.rect(screen, BLUE, self.socket)
        pygame.draw.rect(screen, GRAY, self.battery)

        pygame.draw.line(screen, BLACK,
                         self.socket.center,
                         self.server.center,4)

        pygame.draw.line(screen, BLACK,
                         self.battery.center,
                         self.server.center,4)

        font = pygame.font.SysFont(None,30)

        screen.blit(font.render("Server",True,BLACK),(515,140))
        screen.blit(font.render("Socket",True,BLACK),(75,150))
        screen.blit(font.render("Battery",True,BLACK),(75,380))


system = PowerSystem()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    system.draw(screen)

    pygame.display.flip()

pygame.quit()
