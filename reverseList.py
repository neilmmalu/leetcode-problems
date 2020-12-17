# Reverse a singly linked list.

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    if not head:
        return head
    if not head.next:
        return head

    prev, curr = head, head.next
    prev.next = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

if __name__ == "__main__":
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    rev = reverseList(n1)
    print(n1.next)
