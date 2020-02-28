import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

multiplier = 4
height, width = 200 * multiplier, 300 * multiplier

running = True
count = 0
coordinates = []
pygame.init()
display = pygame.display.set_mode((width, height))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10 * multiplier)
ticks = 400
clock = pygame.time.Clock()

hexagon = [((25 * multiplier), height - (185 * multiplier)), ((75 * multiplier), height - (185 * multiplier)),
           ((100 * multiplier), height - (150 * multiplier)), ((75 * multiplier), height - (120 * multiplier)),
           ((50 * multiplier), height - (150 * multiplier)), ((20 * multiplier), height - (120 * multiplier))]
rectangle = [((95 * multiplier), height - (30 * multiplier)), ((30 * multiplier), height - (68 * multiplier)),
             ((35 * multiplier), height - (77 * multiplier)), ((100 * multiplier), height - (38 * multiplier))]
diamond = [((225 * multiplier), height - (10 * multiplier)), ((200 * multiplier), height - (25 * multiplier)),
           ((225 * multiplier), height - (40 * multiplier)), ((250 * multiplier), height - (25 * multiplier))]
ellipse = [(110 * multiplier), (height - (140 * multiplier)), (80 * multiplier), (40 * multiplier)]


def draw():
    pygame.draw.polygon(display, (138, 132, 226), hexagon)
    pygame.draw.polygon(display, (138, 132, 226), rectangle)
    pygame.draw.polygon(display, (138, 132, 226), diamond)
    pygame.draw.circle(display, (138, 132, 226), ((225 * multiplier), height - (150 * multiplier)), 25 * multiplier)
    pygame.draw.ellipse(display, (138, 132, 226), pygame.Rect(ellipse))
    if count > 0:
        pygame.draw.rect(display, (0, 0, 255),
                         pygame.Rect(coordinates[0][0], coordinates[0][1], multiplier, multiplier))
        textsurface = myfont.render("Initial Postion", False, (255, 0, 0))
        display.blit(textsurface, (coordinates[0][0] - 10 * multiplier, coordinates[0][1] + multiplier))
    if count > 1:
        pygame.draw.rect(display, (0, 0, 255),
                         pygame.Rect(coordinates[1][0], coordinates[1][1], multiplier, multiplier))
        textsurface = myfont.render("Goal Postion", False, (255, 0, 0))
        display.blit(textsurface, (coordinates[1][0] - 10 * multiplier, coordinates[1][1] + multiplier))
    pygame.display.flip()


def animate(travelList):
    display.fill((0,0,0))
    for x, y in travelList:
        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * multiplier, y * multiplier, multiplier, multiplier))
        draw()
        pygame.display.flip()
        clock.tick(ticks)


# while count < 2:
#     display.fill((0, 0, 0))
#     draw()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONUP:
#             x, y = pygame.mouse.get_pos()
#             coordinates.append([x, y])
#             count += 1
# draw()

# listx = [[x, x] for x in range(150)]
# animate(listx)


pygame.time.wait(3000)
pygame.quit()
exit()
