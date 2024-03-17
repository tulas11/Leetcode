class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        start=0
        end=len(s)-1
        vowels="aeiouAEIOU"
        while start<end:
            if s[start] not in vowels:
                start+=1
            elif s[end] not in vowels:
                end-=1
            else:
                s[start], s[end]= s[end], s[start]
                start+=1
                end-=1
        return "".join(s)

            


    