from Mechanism import Environment, Node


class Dijkstra:
    def __init__(self, start, goal, clearance):
        self.start = start
        self.goal = goal
        self.clearance = clearance

    def solve(self):
        search = []
        CurrentNode = Node(self.start)
        NodeList = [CurrentNode]
        NodeDict = {tuple(CurrentNode.env)}
        while CurrentNode.env != self.goal:
            if len(NodeList) > 0:
                CurrentNode = NodeList.pop()
                search.append(CurrentNode.env)
                Course = Environment(CurrentNode.env, self.clearance)
                for action in Course.possibleMoves():
                    temp = Course.move(action)
                    tempNode = Node(temp.currentPosition, CurrentNode, action)
                    if tuple(tempNode.env) not in NodeDict:
                        NodeList.append(tempNode)
                        NodeDict.add(tuple(tempNode.env))
                NodeList.sort(key=lambda x: x.weight, reverse=True)
            else:
                return -1, CurrentNode.path(), search
        x = CurrentNode.path()
        path = []
        for node in x:
            path.append(node.env)
        return path, search
