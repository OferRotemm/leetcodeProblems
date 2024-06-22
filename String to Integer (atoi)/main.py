def myAtoi(s):
        inte = ""
        def intCheck(x,y): # x = str begins with a number , y = '+' or '-' or empty
            inteC = ""

            def rangCheck(z,y):
                r = 2**31
                if y == "-":
                    if int(y + z) >= -r:
                        return y + z
                    else: return str(-r)
                else:
                    if int(z) <= r - 1:
                        return z
                    else: return str(r - 1)
           
            for i in range(len(x)):
                    if len(inteC) > 10:
                        inteC = str(0 + int(inteC))
                        if len(inteC) > 10:
                             return int(rangCheck(inteC,y))
                        else:
                             inteC += x[i]
                    elif x[i].isdecimal():
                        inteC += x[i]
                    else: 
                        if len(inteC) == 10:
                                return int(rangCheck(inteC,y))
                        else: return int(y + inteC)
            if len(inteC) >= 10:
                             return int(rangCheck(inteC,y))
            return 0 + int(y + inteC)
               
        for i in s:
            if inte == "":
                if i == " ":
                    continue
                elif i == "+" or i == "-":
                    inte += i
                elif i.isdecimal(): 
                    return 0 + intCheck(s[s.index(i):], inte)
                else: return 0
            else:
                if i.isdecimal(): 
                    return 0 + intCheck(s[s.index(i):], inte)
                else: return 0
        return 0
        """
        :type s: str
        :rtype: int
        """
      

a = " + 5" 
b = "0052.36" 
c = "42" 
d =  "-042"
e = " ktd4567 "
f = "0"
g = ""
h = "   +0052525259999999999999"
i = "-9999999999"
j = "5-3258 "
k = "6w"
l = "."
m = " "
n = "+a"
o = "      -11919730356x"
p = " 0000000000000000200"
q = " -0000000000000000200"
r = "  0000000000012345678"

print("----------")
print(myAtoi(a))
print(myAtoi(b))
print(myAtoi(c))
print(myAtoi(d))
print(myAtoi(e))
print(myAtoi(f))
print(myAtoi(g))
print(myAtoi(h))
print(myAtoi(i))
print(myAtoi(j))
print(myAtoi(k))
print(myAtoi(l))
print(myAtoi(m))
print(myAtoi(n))
print(myAtoi(o))
print(myAtoi(p))
print(myAtoi(q))
print(myAtoi(r))
print("----------")