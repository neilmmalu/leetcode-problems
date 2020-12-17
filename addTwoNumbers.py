# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0

        total = l1Val + l2Val + carry
        if total > 9:
            carry = 1
            total = total % 10
        else:
            carry = 0
        
        newNode = ListNode(total)
        curr.next = newNode
        curr = newNode
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry:
        newNode = ListNode(1)
        curr.next = newNode
    return dummy.next

if __name__ == "__main__":
    m3 = ListNode(9)
    m2 = ListNode(4, m3)
    m1 = ListNode(2, m2)

    n3 = ListNode(9)
    n2 = ListNode(6, n3)
    n1 = ListNode(5, n2)

    print(addTwoNumbers(m1, n1).next.next.next.val)

        
