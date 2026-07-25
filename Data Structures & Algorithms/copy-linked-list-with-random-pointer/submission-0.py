"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        camp = { None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            camp[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = camp[curr]
            copy.next = camp[curr.next]
            copy.random = camp[curr.random]
            curr = curr.next
        
        return camp[head]
        