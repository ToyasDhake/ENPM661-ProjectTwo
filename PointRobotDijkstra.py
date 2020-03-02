from PointRobotMechanism import Environment, Node


class Dijkstra:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def solve(self):
        search = []
        CurrentNode = Node(self.start)
        NodeList = [CurrentNode]
        NodeDict = {tuple(CurrentNode.env)}
        while CurrentNode.env != self.goal:
            CurrentNode = NodeList.pop()
            search.append(CurrentNode.env)
            Course = Environment(CurrentNode.env)
            for action in Course.possibleMoves():
                temp = Course.move(action)
                tempNode = Node(temp.currentPosition, CurrentNode, action)
                if tuple(tempNode.env) not in NodeDict:
                    NodeList.append(tempNode)
                    NodeDict.add(tuple(tempNode.env))
            NodeList.sort(key=lambda x: x.weight, reverse=True)

        x = CurrentNode.path()
        path = []
        for node in x:
            path.append(node.env)
        return path, search
