from Mechanism import Environment
from Mechanism import Node
from operator import itemgetter

start = [3, 6]
goal = [20,4]

CurrentNode = Node(start)
NodeList = [CurrentNode]
NodeDict = {tuple(CurrentNode.env)}

while CurrentNode.env != goal:
    
    CurrentNode = NodeList.pop()
    
    Course = Environment(CurrentNode.env)
    
    for action in Course.possibleMoves():
        temp = Course.move(action)
        tempNode = Node(temp.currentPosition,CurrentNode,action)
        if tuple(tempNode.env) not in NodeDict:
            NodeList.append(tempNode)
            NodeDict.add(tuple(tempNode.env))
   
    NodeList.sort(key=lambda x: x.weight, reverse=True)
    #print(CurrentNode.env)

x = CurrentNode.path()
for node in x:
    print(node.env)

        




