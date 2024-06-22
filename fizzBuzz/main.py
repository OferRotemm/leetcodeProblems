def fizzBuzz(n):
    i = 1
    x = []
    while i <= n:
        if i % 3 == 0:
            if i % 5 == 0:
                x.append("FizzBuzz")
            else:
                x.append("Fizz")
        elif i % 5 == 0:
            x.append("Buzz")
        else: 
            x.append(f"{i}")
        i +=1  
    else: 
        return x

#print (fizzBuzz(15))

def fizzBuzz2(n):
    x = []
    for i in range(1,n+1,1):
        if i % 3 == 0:
            if i % 5 == 0:
                x.append("FizzBuzz")
            else:
                x.append("Fizz")
        elif i % 5 == 0:
            x.append("Buzz")
        else: 
            x.append(f"{i}")
        i +=1  
    else: 
        return x

print (fizzBuzz2(15))
