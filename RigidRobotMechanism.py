from copy import deepcopy
from math import sqrt

class Node:
    def __init__(self, env, parent=None, action=None):
        self.env = env
        self.parent = parent
        self.action = action
        if action is not None:
            self.weight = parent.weight + sqrt(len(action))
        else:
            self.weight = 0

    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    def actions(self):
        if self.action is None:
            return self.env.possibleMoves()
        else:
            return self.env.possibleMoves(self.action)


class Environment:
    def __init__(self, currentPosition, clearance):
        self.currentPosition = currentPosition
        self.clearance = clearance

    def insideRectangle(self, position):
        if ((1112 / 13) - ((38 / 65) * (position[0]+self.clearance*0.5))) <= (position[1]+self.clearance*0.866) and (position[1]-self.clearance*0.5) <= (
                ((9 / 5) * (position[0]+self.clearance*0.866)) + 14) and (((8 / 5) * (position[0]-self.clearance*0.866)) - 122) <= (position[1]+self.clearance*0.5) and (position[1]-self.clearance*0.866) <= (
                98 - ((3 / 5) * (position[0]-self.clearance*0.5))):
            return True
        else:
            return False

    def insideCircle(self, position):
        if (position[0] - 225) ** 2 + (position[1] - 150) ** 2 <= (25+self.clearance) ** 2:
            return True
        else:
            return False

    def insideElipse(self, position):
        if ((position[0] - 150) ** 2) / (40 + self.clearance) ** 2 + ((position[1] - 100) ** 2) / (20 + self.clearance) ** 2 <= 1:
            return True
        else:
            return False

    def insideDiamond(self, position):
        if (145 - ((3 / 5) * (position[0]+self.clearance*0.5))) <= (position[1]+self.clearance*0.866) and (((3 / 5) * (position[0]-self.clearance*0.5)) - 125) <= (position[1]+self.clearance*0.866) and (
                175 - ((3 / 5) * (position[0]-self.clearance*0.5))) >= (position[1]-self.clearance*0.866) and (((3 / 5) * (position[0]+self.clearance*0.5)) - 95) >= (position[1]-self.clearance*0.866):
            return True
        else:
            return False

    def insidePoly(self, position):
        temp  = False
        if (((position[0]-self.clearance*0.7071) + 100) <= (position[1]+self.clearance*0.7071) and (((7 / 5) * position[0]) + 80) <= position[1] and 185  >= position[1] - self.clearance*1
            and (13 * (position[0]+self.clearance*0.997) - 140) >= (position[1]-self.clearance*0.07672)) or ((((7 / 5) * position[0]) + 80) >= position[1]
                                                             and (290 - ((7 / 5) * (position[0]-self.clearance*0.8137))) >= (position[1]-self.clearance*0.5812) and (
                                                                     (6 / 5) * (position[0]-self.clearance*0.7682) + 30) <= (position[1]+self.clearance*0.64023)
                                                             and (210 - (6 / 5) * (position[0]+self.clearance*0.7682)) <= (position[1]+self.clearance*0.64023)):
            temp =  True
        if (((7 / 5) * position[0]) + 80) >= position[1] and (210 - (6 / 5) * (position[0]+self.clearance*0.7682)) >= (position[1]+self.clearance*0.64023) and ((position[0]-self.clearance*0.7071) + 100) <= (position[1]+self.clearance*0.7071):
            temp =  True

        return temp

    def possiblePostion(self, position):
        possiblity = True
        if position[0] < self.clearance:
            possiblity = False
        if position[1] < self.clearance:
            possiblity = False
        if position[0] > 300 - self.clearance:
            possiblity = False
        if position[1] > 200 - self.clearance:
            possiblity = False
        if self.insideRectangle(position):
            possiblity = False
        if self.insideCircle(position):
            possiblity = False
        if self.insideElipse(position):
            possiblity = False
        if self.insideDiamond(position):
            possiblity = False
        if self.insidePoly(position):
            possiblity = False
        return possiblity

    def possibleMoves(self, remove='A'):
        actions = []
        if self.possiblePostion([self.currentPosition[0], self.currentPosition[1] + 1]):
            actions.append('U')
        if self.possiblePostion([self.currentPosition[0], self.currentPosition[1] - 1]):
            actions.append('D')
        if self.possiblePostion([self.currentPosition[0] - 1, self.currentPosition[1]]):
            actions.append('L')
        if self.possiblePostion([self.currentPosition[0] + 1, self.currentPosition[1]]):
            actions.append('R')
        if self.possiblePostion([self.currentPosition[0] - 1, self.currentPosition[1] + 1]):
            actions.append('UL')
        if self.possiblePostion([self.currentPosition[0] + 1, self.currentPosition[1] + 1]):
            actions.append('UR')
        if self.possiblePostion([self.currentPosition[0] - 1, self.currentPosition[1] - 1]):
            actions.append('DL')
        if self.possiblePostion([self.currentPosition[0] + 1, self.currentPosition[1] - 1]):
            actions.append('DR')
        if remove == 'U' and 'D' in actions:
            actions.remove('D')
        if remove == 'D' and 'U' in actions:
            actions.remove('U')
        if remove == 'L' and 'R' in actions:
            actions.remove('R')
        if remove == 'R' and 'L' in actions:
            actions.remove('L')
        if remove == 'UL' and 'DR' in actions:
            actions.remove('DR')
        if remove == 'UR' and 'DL' in actions:
            actions.remove('DL')
        if remove == 'DL' and 'UR' in actions:
            actions.remove('UR')
        if remove == 'DR' and 'UL' in actions:
            actions.remove('UL')
        return actions

    def move(self, val):
        temp = deepcopy(self)
        if val == 'U':
            temp.currentPosition[1] += 1
        if val == 'D':
            temp.currentPosition[1] -= 1
        if val == 'R':
            temp.currentPosition[0] += 1
        if val == 'L':
            temp.currentPosition[0] -= 1
        if val == 'UL':
            temp.currentPosition[0] -= 1
            temp.currentPosition[1] += 1
        if val == 'UR':
            temp.currentPosition[0] += 1
            temp.currentPosition[1] += 1
        if val == 'DL':
            temp.currentPosition[0] -= 1
            temp.currentPosition[1] -= 1
        if val == 'DR':
            temp.currentPosition[0] += 1
            temp.currentPosition[1] -= 1
        return temp
