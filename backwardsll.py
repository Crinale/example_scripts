def reverse(head):
    prevNode = None
    nextNode = None
    while head is not None:
        nextNode = head.next;
        head.next = prevNode;
        prevNode = head;
        head = nextNode;
    head = prevNode
    return head