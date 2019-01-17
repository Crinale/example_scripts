#levelOrder(BinaryTree t) {
#    if(t is not empty) {
#        // enqueue current root
#        queue.enqueue(t)
#        
#        // while there are nodes to process
#        while( queue is not empty ) {
#            // dequeue next node
#            BinaryTree tree = queue.dequeue();
#            
#            process tree's root;
#            
#            // enqueue child elements from next level in order
#            if( tree has non-empty left subtree ) {
#                queue.enqueue( left subtree of t )
#            }
#            if( tree has non-empty right subtree ) {
#                queue.enqueue( right subtree of t )
#            }
#        }
#    } 
#} 

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
         #Write your code here
           if root:
            q = [root]
            for current in q:
                if current:
                    print(current.data),

                    q.append(current.left)
                    q.append(current.right)


T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)