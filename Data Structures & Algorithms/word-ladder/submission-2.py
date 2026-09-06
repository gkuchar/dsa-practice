from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = wordList
        words.append(beginWord)
        graph = {word : [] for word in words}

        for word in words:
            for i in range(len(word)):
                pre = word[:i]
                post = word[i + 1:]

                new_word = pre + '*' + post

                graph[word].append(new_word)

                if new_word in graph:
                    graph[new_word].append(word)
                else:
                    graph[new_word] = [word]

        def bfs_shortest_path(start):
            count = 1
            visited = set([start])
            q = deque([start])
            true_edge = False

            while q:
                if true_edge: count += 1
                for _ in range(len(q)):
                    curr = q.popleft()
                    for adj in graph[curr]:
                        if adj == endWord:
                            return count
                        if adj not in visited:
                            q.append(adj)
                            visited.add(adj)
                true_edge = not true_edge
            
            return 0


        return bfs_shortest_path(beginWord)
        # T = O(V * w^2), V = len(words) w = len(word)
        # S = O(V * w^2)