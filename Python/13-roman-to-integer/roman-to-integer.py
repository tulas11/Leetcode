class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        d={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i<len(s)-1 and d[s[i]] < d[s[i+1]]:
                count-=d[s[i]]
            else:
                count+=d[s[i]]
        return count
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         value = 0
#         prev = 0
#         for ch in s:
#             if ch == 'I':
#                 value += 1
#                 prev = 1
#             elif ch == 'V':
#                 value += 3 if prev == 1 else 5
#                 prev = 5
#             elif ch == 'X':
#                 value += 8 if prev == 1 else 10
#                 prev = 10
#             elif ch == 'L':
#                 value += 30 if prev == 10 else 50
#                 prev = 50
#             elif ch == 'C':
#                 value += 80 if prev == 10 else 100
#                 prev = 100
#             elif ch == 'D':
#                 value += 300 if prev == 100 else 500
#                 prev = 500
#             elif ch == 'M':
#                 value += 800 if prev == 100 else 1000
#                 prev = 1000
#         return value

        