# given two string a = "abc" b = "sql" merge these two string and form a new string s=[]

class Solution:

    def mergetwoarray(self, word1: str, word2: str) -> list:

        A, B = len(word1), len(word2)

        a, b = 0, 0

        s = []

        word = 1 

        while a < A and b < B:

            if word == 1:

                s.append(word1[a])

                a += 1

                word = 2

            else:
                s.append(word2[b])

                b += 1

                word = 1

        s.extend(word1[a:])

        s.extend(word2[b:])

        return ''.join(s)
    
obj = Solution()

print(obj. mergetwoarray("abc","nbd"))




