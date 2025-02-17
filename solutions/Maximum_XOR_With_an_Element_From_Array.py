class TrieNode:
    def __init__(self):
        self.children = {}

def insert(root, num):
    node = root
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if bit not in node:
            node[bit] = TrieNode()
        node = node[bit]

def query(root, num):
    node = root
    ans = 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if 1 - bit in node:
            bit = 1 - bit
        else:
            bit = bit
        ans = ans * 2 + bit
        node = node[bit]
    return ans

def findMaximumXOR(nums):
    root = TrieNode()
    max_xor = 0
    for num in nums:
        insert(root, num)
        xor_val = query(root, ~num & ((1 << 32) - 1))
        max_xor = max(max_xor, xor_val)
    return max_xor