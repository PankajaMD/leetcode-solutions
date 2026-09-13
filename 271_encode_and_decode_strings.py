class Codec:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(258)
        
        separate = chr(257)
        sb = []
        for s in strs:
            sb.append(s)
            sb.append(separate)
        
        result = "".join(sb)
        result = result[:-1]  # remove the trailing separator
        return result
    
    def decode(self, s: str) -> List[str]:
        if s == chr(258):
            return []
        
        separate = chr(257)
        return s.split(separate)
