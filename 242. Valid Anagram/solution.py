def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
       
        arr2 =[0]*26
        for c in s:
            arr2[ord(c)-97]+=1
        for c in t:
            arr2[ord(c)-97]-=1
            if arr2[ord(c)-97]<0:
                return False
        return True