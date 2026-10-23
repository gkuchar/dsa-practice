from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        counts = Counter(s)

        length = 1
        curr = set()
        for char in s:
            curr.add(char)
            counts[char] -= 1
            if counts[char] == 0:
                curr.remove(char)
                if len(curr) == 0:
                    res.append(length)
                    length = 1
                    continue
            length += 1

        return res
        # T = O(n), n = len(s)
        # S = O(d), d = number of distinct chars in s, or, O(26)
        