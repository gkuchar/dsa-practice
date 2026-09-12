class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        graph = { char : set() for word in words for char in word}

        def find_edge(word1, word2):
            if word1 and not word2: return None, None
            if word1[0] == word2[0]:
                if len(word1) == 1 and len(word2) > 1:
                    return word1, word2[1]
                else:
                    if len(word2) == 1:
                        word2_suf = None
                    else:
                        word2_suf = word2[1:]
                    return find_edge(word1[1:], word2_suf)
            return word1[0], word2[0]

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if w1 == w2: continue

            u, v = find_edge(w1, w2)
            if not u: return ""
            if v != u and v not in graph[u]:
                graph[u].add(v)
        
        print(graph)
        result = []
        seen = set()
        path = set()
        def dfs(char):
            for adj in graph[char]:
                if adj in path:
                    return True
                if adj not in seen:
                    path.add(adj)
                    seen.add(adj)
                    cycle = dfs(adj)
                    if cycle: return True
                    path.remove(adj)
            if char not in result:
                result.append(char)
            return False
        
        for char in graph:
            if dfs(char):
                return ""
        
        result = result[::-1]
        return "".join(result)
