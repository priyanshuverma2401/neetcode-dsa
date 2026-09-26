class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "null00"
        return "___joing___".join(ele for ele in strs)

    def decode(self, s: str) -> List[str]:
        if s == "null00": return []
        return s.split("___joing___")
