from math import log2,ceil

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        self.height=None
def print_inorder(node):
    if node == None:return
    print_inorder(node.left)
    print("",node.key, end="")
    print_inorder(node.right)

class BinarySearchTree:
    def __init__(self,height):
        self.root=None
        self.height=height

    def delete(self,key):
        find_node=find(self,key)
        isLeft=False
        if find_node.parent.left==find_node:
            isLeft=True
        if find_node.left is None and find_node.right is None:
            if isLeft:find_node.parent.left=None
            else:find_node.parent.right=None
        elif find_node.left is None:
            find_node.right.parent=find_node.parent
            if isLeft:find_node.parent.left=find_node.right
            else:find_node.parent.right=find_node.right
        elif find_node.right is None:
            find_node.left.parent=find_node.parent
            if isLeft:find_node.parent.left=find_node.left
            else:find_node.parent.right=find_node.left
        else:
            find_node.key=find_node.right.key
            self.delete(find_node.right.key)
        return find_node.key
    
def MakeEmptyChild(node):
    if node.height==1:return
    node.left=Node(None)
    node.left.parent=node
    node.left.height=node.left.parent.height-1
    node.right=Node(None)
    node.right.parent=node
    node.right.height=node.right.parent.height-1
    MakeEmptyChild(node.left)
    MakeEmptyChild(node.right)

def findNext(node,key):
    if node.key<key:return node
    else: findNext(node.parent,key)

def find(tree,key):
    current=tree.root
    while current is not None:
        temp=current
        if key<current.key:
            current=current.left
        elif key>current.key:
            current=current.right
        else:
            return current
    return findNext(temp,key)

n=0
import queue
qu=queue.Queue()
def BFS(node):
    global qu
    if node==None:return
    qu.put(node)
    while not qu.empty:
        now=qu.get()
        print(f'{now.depth} : ',now.key,end=' ')
        qu.put(now.left)
        qu.put(now.right)
def solution(k, room_number):
    answer = []
    height=ceil(log2(k+1))
    tree=BinarySearchTree(height)
    tree.root=Node(None)
    tree.root.height=height
    MakeEmptyChild(tree.root)
    def set_inorder(node):
        global n
        if node == None:return
        set_inorder(node.left)
        n+=1
        if n>=k+1:return
        node.key=n
        node.depth=node.parent.depth+1
        set_inorder(node.right)
    set_inorder(tree.root)
    BFS(tree.root)
    #print_inorder(tree.root)
    # for i in room_number:
    #     answer.append(tree.delete(i))
    # return answer
solution(10,[1,3,4,1,3,1])