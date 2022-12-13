# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
            
        if len(l) > 1:
            lenth = len(l) // 2
            lr = list(l[len(l)-lenth:])
            lr.reverse()
            if l[:lenth] != lr:
                return False
            
        return True

print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))