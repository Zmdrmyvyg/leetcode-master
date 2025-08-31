# 两个指针思想，中间间隔n+1。
# 对.next做操作才能改变链表结构
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = ListNode(0, head)  # 在链表头加了一个节点0，这样好删除原先的头节点，注意最后要head.next才是真正要的链表头
        slow = head
        fast = head
        
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next  # 只有对.next做操作才能改变链表结构
        
        slow.next = slow.next.next
        return head.next


# --------- 测试用例 -------------
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def linkedlist_to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

if __name__ == "__main__":
    # 示例 1
    head = list_to_linkedlist([1,2,3,4,5])
    n = 2
    new_head = Solution().removeNthFromEnd(head, n)
    print(linkedlist_to_list(new_head))  # 期望输出: [1,2,3,5]

    # 示例 2
    head = list_to_linkedlist([1])
    n = 1
    new_head = Solution().removeNthFromEnd(head, n)
    print(linkedlist_to_list(new_head))  # 期望输出: []

    # 示例 3
    head = list_to_linkedlist([1,2])
    n = 1
    new_head = Solution().removeNthFromEnd(head, n)
    print(linkedlist_to_list(new_head))  # 期望输出: [1]