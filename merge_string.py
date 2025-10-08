# given two string a = "abc" b = "sql" merge these two string and form a new string s=[]

class solution:

    def mergetwoarray(self,word1:str,word2:str)->str:

        A,B = len(word1),len(word2)

        a,b = 0,0

        s = []

     

        while a < A and b < B:

            word = 1

            s.append(word1[a])

            a+= 1

            word = 2

        else:

            s.append(word[a])

            b += 1

            word = 1

        




