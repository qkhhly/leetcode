# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        
        
        res = ListNode(x=l1.val + l2.val)
        
        if res.val >= 10:
            res.val -= 10
            carry = 1
        else:
            carry = 0
            
        p = res
        p1 = l1.next
        p2 = l2.next
        while p1 is not None and p2 is not None:
            r = ListNode(0)
            r.val = p1.val + p2.val + carry
            
            if r.val >= 10:
                r.val -= 10
                carry = 1
            else:
                carry = 0
            
            p1 = p1.next
            p2 = p2.next
            p.next = r
            p = r
        
        m = p2 if p1 is None else p1
        
        if m is None:
            if carry == 1:
                r = ListNode(1)
                p.next = r
        else:
            r = ListNode(0)
            r.val = m.val + carry
            if r.val >= 10:
                r.val -= 10
                carry = 1
            else:
                carry = 0
            p.next = r
            p = r
            m = m.next
            while m is not None:
                r = ListNode(m.val + carry)
                if r.val >= 10:
                    r.val -= 10
                    carry = 1
                else:
                    carry = 0
                p.next = r
                p = r
                m = m.next
        
        if carry == 1:
            p.next = ListNode(1)
        
        return res
            
            
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        ''' addTwoNumbers recursively'''

        def add(n1, n2, carry):

            if n1 is None and n2 is None and carry == 0:
                return None

            p = ListNode(carry)
            if n1 is not None:
                p.val += n1.val 
            if n2 is not None:
                p.val += n2.val 

            if p.val >= 10:
                p.val -= 10
                carry = 1
            else:
                carry = 0 


            p.next = add(n1.next if n1 is not None else None, n2.next if n2 is not None else None, carry)
            
            return p








