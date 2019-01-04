def insertNodeAtHead(llist, data):
    # Write your code here
    nodePrev = SinglyLinkedListNode(data)
    nodePrev.next = llist
    llist = nodePrev
    return llist