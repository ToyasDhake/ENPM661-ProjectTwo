from Dijkstra import Dijkstra
from Mechanism import Environment
from AStar import AStar
from time import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


pointRobot = False
aStar = False
manual = False
if len(sys.argv)>1:
    if '-p' in sys.argv:
        pointRobot = True
    if '-a' in sys.argv:
        aStar = True
    if '-m' in sys.argv:
        manual = True

if pointRobot:
    clearance = 0
    radius = 0
else:
    radius = int(input("Enter radius: "))
    clearance = int(input("Enter Clearance: "))
    clearance += radius

multiplier = 4
height, width = 200 * multiplier, 300 * multiplier

running = True
count = 0
coordinates = []

env = Environment([0,0], clearance)
startBool = True
goalBool = True
if manual:
    while startBool:
        startPos = input("Enter start position: ")
        startPos = startPos.replace(" ", "")
        startPos = startPos.split(",")
        if env.possiblePostion([int(startPos[0]), 200-int(startPos[1])]):
            coordinates.append([int(startPos[0])*multiplier, (200-int(startPos[1]))*multiplier])
            count += 1
            startBool = False
        else:
            print("Invalid position.")
    while goalBool:
        goalPos = input("Enter goal position: ")
        goalPos = goalPos.replace(" ", "")
        goalPos = goalPos.split(",")
        if env.possiblePostion([int(goalPos[0]), 200-int(goalPos[1])]):
            coordinates.append([int(goalPos[0])*multiplier, (200-int(goalPos[1]))*multiplier])
            count += 1
            goalBool = False
        else:
            print("Invalid position.")


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
ellipse = [(110 * multiplier), (height - (120 * multiplier)), (80 * multiplier), (40 * multiplier)]


def draw():
    global count
    pygame.draw.polygon(display, (138, 132, 226), hexagon)
    pygame.draw.polygon(display, (138, 132, 226), rectangle)
    pygame.draw.polygon(display, (138, 132, 226), diamond)
    pygame.draw.circle(display, (138, 132, 226), ((225 * multiplier), height - (150 * multiplier)), 25 * multiplier)
    pygame.draw.ellipse(display, (138, 132, 226), pygame.Rect(ellipse))
    if count > 0:
        env = Environment(coordinates[0], clearance)
        if env.possiblePostion([int(coordinates[0][0] / multiplier), int(200 - coordinates[0][1] / multiplier)]):
            if radius != 0:
                pygame.draw.circle(display, (0, 0, 255), (coordinates[0][0], coordinates[0][1]), radius * multiplier, 1)
            pygame.draw.rect(display, (0, 0, 255),
                             pygame.Rect(coordinates[0][0], coordinates[0][1], multiplier, multiplier))



            textsurface = myfont.render("Initial Postion", False, (255, 0, 0))
            if height - coordinates[0][1] > 40:
                display.blit(textsurface, (coordinates[0][0] - 10 * multiplier, coordinates[0][1] + multiplier))
            else:
                display.blit(textsurface, (coordinates[0][0] - 10 * multiplier, coordinates[0][1] + multiplier - 40))
        else:
            print("Invalid position")
            count = 0
            coordinates.pop(0)

    if count > 1:
        env = Environment(coordinates[1], clearance)
        if env.possiblePostion([int(coordinates[1][0] / multiplier), int(200 - coordinates[1][1] / multiplier)]):
            if radius != 0:
                pygame.draw.circle(display, (0, 0, 255), (coordinates[1][0], coordinates[1][1]), radius * multiplier, 1)
            pygame.draw.rect(display, (0, 0, 255),
                             pygame.Rect(coordinates[1][0], coordinates[1][1], multiplier, multiplier))


            textsurface = myfont.render("Goal Postion", False, (255, 0, 0))
            if height - coordinates[1][1] > 40:
                display.blit(textsurface, (coordinates[1][0] - 10 * multiplier, coordinates[1][1] + multiplier))
            else:
                display.blit(textsurface, (coordinates[1][0] - 10 * multiplier, coordinates[1][1] + multiplier - 40))
        else:
            print("Invalid position")
            count = 1
            coordinates.pop(1)
    pygame.display.flip()
    clock.tick(ticks)


def animate(travelList):
    speed = int((len(travelList) - 1000)*15/50000 + 5)
    display.fill((0, 0, 0))
    length = len(travelList)
    loops = int(length/speed)
    offset = length - length*speed
    for i in range(loops):
        pygame.event.get()
        for j in range(speed):
            index = i*speed+j
            pygame.draw.rect(display, (255, 255, 255),
                             pygame.Rect(travelList[index][0] * multiplier, height - travelList[index][1] * multiplier, multiplier, multiplier))
        draw()
        pygame.display.flip()
        clock.tick(ticks)
    for i in range(offset):
        pygame.event.get()
        pygame.draw.rect(display, (255, 255, 255),
                         pygame.Rect(travelList[i+loops*speed][0] * multiplier, height - y[i+loops*speed] * multiplier,
                                     multiplier, multiplier))
    draw()
    pygame.display.flip()
    clock.tick(ticks)


def animatePath(travelList):
    display.fill((0, 0, 0))
    for x, y in travelList:
        pygame.draw.rect(display, (0, 255, 0),
                         pygame.Rect(x * multiplier, height - y * multiplier, multiplier, multiplier))
        draw()
        pygame.display.flip()
        clock.tick(ticks)

if not manual:
    while count < 2:
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                coordinates.append([x, y])
                count += 1
        draw()

draw()
if aStar:
    start = time()
    aStar = AStar([int(coordinates[0][0] / multiplier), int(200 - coordinates[0][1] / multiplier)],
                        [int(coordinates[1][0] / multiplier), int(200 - coordinates[1][1] / multiplier)], clearance)
    solution = aStar.solve()
    if len(solution) == 3:
        animate(solution[2])
        print("Unreachable goal.")
    else:
        path, search = solution[0], solution[1]
        end = time()
        print("It took {} seconds to solve.".format(end - start))
        animate(search)

        animatePath(path)

        pygame.time.wait(3000)
else:
    start = time()
    dijkstra = Dijkstra([int(coordinates[0][0] / multiplier), int(200 - coordinates[0][1] / multiplier)],
                        [int(coordinates[1][0] / multiplier), int(200 - coordinates[1][1] / multiplier)], clearance)
    solution = dijkstra.solve()
    if len(solution) == 3:
        animate(solution[2])
        print("Unreachable goal.")
    else:
        path, search = solution[0], solution[1]
        end = time()
        print("It took {} seconds to solve.".format(end - start))
        animate(search)

        animatePath(path)

        pygame.time.wait(3000)
pygame.quit()
exit()
