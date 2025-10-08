# given two string a = "abc" b = "sql" merge these two string and form a new string s=[]

class solution:

    def mergetwoarray(self,word1:str,word2:str)->str:

        A,B = len(word1),len(word2)

        a,b = 0,0

        s = []

        word = 1

        if a < A and b < B:

            