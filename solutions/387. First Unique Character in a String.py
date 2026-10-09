class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Hashmaps + Queues
        count = defaultdict(int)
        q = deque()
        
        for i in range(len(s)):
            count[s[i]] += 1
            q.append(i)
        print(count)
        print(q)
        while q and count[s[q[0]]] > 1:
            q.popleft()
        return q[0] if q else -1
