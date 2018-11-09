#!/bin/python

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    if head == None:
        return SinglyLinkedListNode(data)
    else:
        newnode = SinglyLinkedListNode(data)
        newnode.next = head
        return newnode

def insertNodeAtTail(head, data):
    #need something that will allow it to reference what llist is.
    #base case if there is nothing at all in the linked list
    if head == None:
        return SinglyLinkedListNode(data)
    else:
    #If there is something in the link list and the next is none add a node
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
        else:
            #if the next node has something keep going until you see none in the next
            insertNodeAtTail(head.next,data)
        return head

def insertNodeAtPosition(head, data, position):
    if head == None:
        return head
    newNode = SinglyLinkedListNode(data)
    count = 0
    curNode = head
    while curNode is not None:
        if count == position-1:
            temp = curNode.next
            curNode.next = newNode
            curNode.next.next = temp
            return head
        curNode = curNode.next
        count += 1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for i in xrange(llist_count):
        llist_item = int(raw_input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()

