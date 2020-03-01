from Mechanism import Environment
from Mechanism import Node
from operator import itemgetter

#Get start node from user
#start = input("Enter Start Position: ")
#start = start.replace(' ', '')
#start = list(map(int,start))

start = [1, 1]
goal = [5, 10]

iterator = 0
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
    iterator +=1
    NodeList.sort(key=lambda x: x.weight, reverse=True)
    #print(CurrentNode.env)

x = CurrentNode.path()
for node in x:
    print(node.env)
if CurrentNode.env == goal:
        print("success")
        




