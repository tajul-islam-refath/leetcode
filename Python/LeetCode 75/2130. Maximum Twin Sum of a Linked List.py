
# Definition for singly-linked list.
# first find middle of linked list
# reverse middle.next to end of the list
# calculate max sum
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        node = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return node

    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head.next.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        reversedHead = self.reverse(right)
        ans = 0
        while reversedHead != None and reversedHead.next != None:
            ans = max((reversedHead.val + head.val), ans)
            head = head.next
            reversedHead = reversedHead.next
        if reversedHead != None:
            ans = max((reversedHead.val + head.val), ans)
        return ans