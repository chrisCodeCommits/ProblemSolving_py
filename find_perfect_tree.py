##### MODULE USED ####################################################################

from binarytree import Node  # to get this module run "pip install binarytree"

#######################################################################################

#class Tree:
#    x = 0
#    l = None
#    r = None

#class Node:
#    x = 0
#    left = None
#    right = None
#
#    def __init__(self, x):
#        self.x = x

#########################################################################################



def remove_unbalanced_nodes(t):
    # Breadth first traversal to find and remove nodes that do not have a sibling
    nodes = [t]
    while nodes:
        n = nodes.pop(0)
        if n.left and not n.right:
            n.left = None
        elif n.right and not n.left:
            n.right = None

        if n.left and n.right:
            nodes.extend([n.left, n.right])

            
            
def has_two_children(t):
    if t.left and t.right:
        return True
    return False
  
  

def prune_short_subtrees(t):
    # Breadth first traversal to find which subtree is bigger, removing the smaller subtree
    nodes = [t]
    while nodes:
        n = nodes.pop(0)
        if not n:
            continue
        if has_two_children(n):
            if has_two_children(n.left) and not has_two_children(n.right):
                n.right = None
            if has_two_children(n.right) and not has_two_children(n.left):
                n.left = None
            nodes.extend([n.left, n.right])
            
            
            
            
############################################################################################
    
    
        
        
    
 ## Solution ####  
            
def size(t):
    # Breadth first traversal to find the size of the tree
    nodes = [t]
    out = 0
    while nodes:
        n = nodes.pop(0)
        if not n:
            continue
        out += 1
        nodes.extend([n.left, n.right])
    return out

 
    
    
    
    
  #############################################################################################  


  
if __name__ == "__main__":
    # build the tree from the example
    t = Node(1)
    t.left = Node(2)
    t.left.right = Node(4)
    t.right = Node(3)
    t.right.left = Node(5)
    t.right.left.left = Node(7)
    t.right.left.right = Node(8)
    t.right.right = Node(6)
    t.right.right.left = Node(9)
    t.right.right.right = Node(10)
    t.right.right.right.left = Node(11)

    print(t) # print out the original tree
    remove_unbalanced_nodes(t)
    print(t)
    prune_short_subtrees(t)
    print(t)

    # special case for finding the bigger subtree on the left or right
    if t.left and not t.right:
        t = t.left
    elif t.right and not t.left:
        t = t.right

    print(t)
    print(size(t))
