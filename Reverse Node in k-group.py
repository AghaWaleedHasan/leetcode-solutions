# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int):
        len_arr = 0

        iterator = head
        while (iterator != None):
            len_arr += 1
            iterator = iterator.next
        
        if (len_arr == 1):
            return(head)
        
        sub_lists = int(len_arr/k) #number of sub arrays
        leftover = len_arr - (sub_lists*k)

        arr = []
        stack = []

        iterator = head
        for i in range(sub_lists):
            for j in range(k):
                stack.append(iterator)
                iterator = iterator.next
            iterator = stack[-1].next
            for j in range(k):
                arr.append(stack.pop())

        while (iterator != None):
            arr.append(iterator)
            iterator = iterator.next


        for i in range(len_arr-1):
            arr[i].next = arr[i+1]
        if (arr[i+1]):
            arr[i+1].next = None

        # print(arr)
        return (arr[0])
