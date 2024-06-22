def divide(dividend, divisor):
        rang = 2**31 -1
        neg = ""
        num1 = abs(dividend)
        num2 = abs(divisor)

        def negCheck(neg, num):
              if neg == "":
                    return num
              else:
                    return 0 - num
              
        if num2 > num1:
                return 0
        if (dividend < 0) or (divisor < 0):
                if (dividend < 0) & (divisor < 0):
                    neg = neg
                else:
                    neg += "neg"
                    rang += 1
        if num1 == num2:
              return negCheck(neg, 1)
        if num2 == 1:
              if num1 > rang:
                return rang
              else:
                   return negCheck(neg, num1)
        else:
            di1 = str(num1)
            di2 = str(num2)
            count = 1
            indx = len(di2) - 1
            result = ""
            longDi = int(di1[0:indx+1])
            safe = rang - num2
            d = num2
            while True:
                  while d < longDi:
                        if d < safe:
                              d += num2
                              count += 1
                        elif d == safe: 
                              count += 1
                        elif d > safe:
                              result += str(count)
                              indx += 1
                              if indx == len(di1):
                                    return negCheck(neg, int(result))
                  if d > longDi:
                        result += str(count - 1)
                        remainder = longDi - (d - num2)
                        count = 1
                        while num2 > remainder:
                              indx += 1
                              if indx == len(di1):
                                    return negCheck(neg, int(result))
                              else:
                                    new_remainder1 = str(remainder)
                                    new_remainder2 = di1[indx]
                                    longDi_str = new_remainder1 + new_remainder2
                                    remainder = int(longDi_str)
                                    longDi = remainder
                                    if longDi > num2:
                                          d = num2
                                    else:
                                          result += "0"
                  elif d == longDi:
                        result += str(count)
                        remainder = 0
                        count = 1
                        while num2 > remainder:
                              indx += 1
                              if indx == len(di1):
                                    return negCheck(neg, int(result))
                              else:
                                    new_remainder1 = str(remainder)
                                    new_remainder2 = di1[indx]
                                    longDi_str = new_remainder1 + new_remainder2
                                    remainder = int(longDi_str)
                                    longDi = remainder
                                    if longDi >= num2:
                                          d = num2
                                    else:
                                          result += "0"
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

a = 0 
b = 30

c=10
d=3

e=7
f=-3

g=-30
h=10

i=2
j=20

k=-1
l=-1

m=2147483647
n=2

o=-2147483648
p=-1

q= 52
r= 36

s=1100540749
t=-1090366779

u=-2147483648
v=4

print("-----------")
print(a/b)
print(divide(a,b))
print("------")
print(c/d)
print(divide(c,d))
print("------")
print(e/f)
print(divide(e,f))
print("------")
print(g/h)
print(divide(g,h))
print("------")
print(i/j)
print(divide(i,j))
print("------")
print(k/l)
print(divide(k,l))
print("------")
print(m/n)
print(divide(m,n))
print("------")
print(o/p)
print(divide(o,p))
print("------")
print(q/r)
print(divide(q,r))
print("------")
print(s/t)
print(divide(s,t))
print("------")
print(u/v)
print(divide(u,v))
print("-----------")

