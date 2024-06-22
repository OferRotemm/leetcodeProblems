def divisorSubstrings(num, k):
        count = 0
        n = str(num)
        start = 0
        for d in n:
            end = start + k -1
            if end == len(n):
                   return count
            check = ""
            for r in range (start, end+1):
                    check += n[r]
            start += 1
            if int(check) == 0:
                   continue
            if num % int(check) == 0:
                   count += 1
        return count
        
        
a = 240
b = 2

c = 430043
d = 2

e = 263
f = 1

g = 245873
h = 6

i = 10000
j = 2

k = 256
l = 1

m = 30003
n = 3


print("-------")
print(divisorSubstrings(a,b)) #2
print(divisorSubstrings(c,d)) #2
print(divisorSubstrings(e,f)) #0
print(divisorSubstrings(g,h)) #1
print(divisorSubstrings(i,j)) #1
print(divisorSubstrings(k,l)) #1
print(divisorSubstrings(m,n)) #1
print("-------")




"""
:type num: int
:type k: int
:rtype: int
"""
