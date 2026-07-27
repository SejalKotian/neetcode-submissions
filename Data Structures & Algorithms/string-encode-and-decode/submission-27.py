class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr =''
        for s in strs:
            encodedstr+=str(len(s))+'#'+s
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            strlength = int(s[i:j])
            decoded.append(s[j+1:j+1+strlength])
            i=j+1+strlength

        return decoded



