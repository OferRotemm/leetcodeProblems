def countValidWords(sentence):
        s = sentence.split()
        count = 0

        def digitscheck(word):
            for l in word:
                if l.isdigit():
                     return "not valid"
            return "valid"
        
        def punccheck(word):
            punc = [".", ",", "!"]
            for s in punc:
                if s in word:
                    if len(word) == 1:
                         return "short"
                    t = word.index(s)
                    if t != len(word) - 1:
                            return "not valid"        
            else: return "valid"
       
        for w in s:
                p = punccheck(w)

                if p == "short":
                       count += 1
                       continue
                elif p == "not valid":
                     continue
                
                d = digitscheck(w)
                
                if d == "not valid":
                     continue
                
                elif "-" in w:
                    if w[0] == "-" or w[len(w)-1] == "-":
                        continue
                    else:
                        l = w.count("-")
                        if l > 1:
                               continue
                        m =  w.index("-")
                        if w[m+1].isalpha():
                             count +=1
                        else:
                             continue
                else: count +=1
        return count


     
        """
        :type sentence: str
        :rtype: int
        """


a = "cat and  dog"
b = "!this  1-s b8d!"
c = "alice and  bob are playing stone-game10"
d = "cat- -and  ,dog"
e = "cat,, and!  dog"
f = "c,a.t a--nd  d-o-g"
g = "c-at! a nd ,   dog"
h = " cat and  dog-,  "

print("----")
print(countValidWords(a)) #3
print(countValidWords(b)) #0
print(countValidWords(c)) #5
print(countValidWords(d)) #0
print(countValidWords(e)) #2
print(countValidWords(f)) #0
print(countValidWords(g)) #5
print(countValidWords(h)) #2
print("----")
