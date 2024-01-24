class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next # set odd.next to current odd
            even.next = odd.next
            even = even.next # set even.next to current even
        odd.next = evenHead
        return head