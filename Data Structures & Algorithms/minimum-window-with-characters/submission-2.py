class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s: return ""

        need_dict = {}
        window_dict = {}
        
        
        
        left, right = 0, 0
        res, resLen = [-1, -1], float("infinity")


        for c in t:
            need_dict[c] = need_dict.get(c, 0) + 1

        have, need = 0, len(need_dict)
        
        while right < len(s):
            c = s[right]

            window_dict[c]  = window_dict.get(c, 0) + 1

            if c in need_dict and window_dict[c] == need_dict[c]:
                have+=1
            
            while have == need:
                if ((right - left) + 1 ) < resLen:
                    resLen = ((right - left) + 1)
                    res = [left, right]
                window_dict[s[left]]-=1
                
                if s[left] in need_dict and window_dict[s[left]] < need_dict[s[left]]:
                    have-=1
                left+=1
            right+=1
        return s[res[0]: res[1]+1] if resLen != float("infinity") else ""

        
        
        


            
                

        