import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

multiplier = 4
height, width = 200 * multiplier, 300 * multiplier

running = True
pygame.init()
display = pygame.display.set_mode((width, height))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)
ticks = 400
clock = pygame.time.Clock()

hexagon = [((25 * multiplier), height - (185 * multiplier)), ((75 * multiplier), height - (185 * multiplier)),
           ((100 * multiplier), height - (150 * multiplier)), ((75 * multiplier), height - (120 * multiplier)),
           ((50 * multiplier), height - (150 * multiplier)), ((20 * multiplier), height - (120 * multiplier))]
rectangle = [((95 * multiplier), height - (30 * multiplier)), ((30 * multiplier), height - (68 * multiplier)),
             ((35 * multiplier), height - (77 * multiplier)), ((100 * multiplier), height - (38 * multiplier))]
diamond = [((225 * multiplier), height - (10 * multiplier)), ((200 * multiplier), height - (25 * multiplier)),
           ((225 * multiplier), height - (40 * multiplier)), ((250 * multiplier), height - (25 * multiplier))]


def draw():
    pygame.draw.polygon(display, (138, 132, 226), hexagon)
    pygame.draw.polygon(display, (138, 132, 226), rectangle)
    pygame.draw.polygon(display, (138, 132, 226), diamond)
    pygame.draw.circle(display, (138, 132, 226), ((225 * multiplier), height - (150 * multiplier)), 25 * multiplier)
    pygame.draw.ellipse(display, (138, 132, 226), pygame.Rect((110 * multiplier), (height - (140 * multiplier)), (80 * multiplier), (40 * multiplier)))
    pygame.display.flip()
    clock.tick(ticks)


draw()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        x, y = pygame.mouse.get_pos()

pygame.quit()
exit()