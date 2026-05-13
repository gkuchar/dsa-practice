class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        mapp = {}

        for s in strs:
            master = str(sorted(s))
            if master in mapp:
                mapp[master].append(s)
            else:
                mapp[master] = [s]
        
        for arr in mapp.values():
            ret.append(arr)

        return ret

        # T = O(klgk)
        # S = O(n)
        