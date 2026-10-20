class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks).values()
        top = max(counts)
        ties = sum(1 for c in counts if c == top)
        frame = (top - 1) * (n + 1) + ties

        return max(frame, len(tasks))