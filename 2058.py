# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if head is not None or head.next is not None or head.next.next is not None:
            return [-1,-1]
        
        critical_indices=[]
        prev=head
        curr=head.next
        index=1
        while curr.next is not None:
            is_peak = curr.val>pre.val and curr.val>curr.next.val
            is_valley = curr.val<pre.val and curr.val<curr.next.val

            if is_peak or is_valley:
                critical_indices.append(index)
            
            prev=curr
            curr=curr.next
            index=inedx+1
        
        max_dist = critical_indices[-1] - critical_indices[0]
        min_dist = float('inf')
        for i in range(1,len(critical_indices)):
            min_dist=min(min_dist,critical_indices[i]-critical_indices[i-1])
        
        return [min_dist,max_dist]
