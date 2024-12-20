class Node:
    def __init__(self , data , score ):
        self.data = data
        self.score = score
        self.right = None
        self.left = None

node1 = Node ("Student" , None)
node2 = Node("Hana" , 10)
node3 = Node("Mohammad", 20)
node4 = Node("Ali" , 17 )
node5 = Node("Majedeh", 20)
node6 = Node("Maha" , 20)
node7 = Node("Mahdi", 18)


node1.right = node2
node1.left = node3
node2.right = node5
node2.left = node6
node3.right = node4
node3.left = node7

print(f"***Main root node is {node1.data}***\n"
      f"Right side of the main root is {node1.right.data} . Score is {node1.right.score}\n"
      f"Left side of the main root is {node1.left.data}. Score is {node1.left.score}\n"
      f"**second node is {node2.data}.Score is {node2.score}**\n"
      f"right side of second root is {node2.right.data}. Score is {node2.right.score}\n"
      f"left side of second root is {node2.left.data}. Score is {node2.left.score}\n"
      f"**third root is {node3.data}.Score is {node3.score}**\n" 
      f"right side of third root is {node3.right.data}. Score is {node3.right.score}\n"
      f"left side of third root is {node3.left.data}. Score is {node3.left.score}\n")

        
        
