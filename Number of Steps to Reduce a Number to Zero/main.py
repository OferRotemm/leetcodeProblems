def numberOfSteps(num):
    s = 0
    while num > 0:
        if num % 2 == 0:
            num/=2
        else: num -=1
        s +=1
    return s

print(numberOfSteps(123))