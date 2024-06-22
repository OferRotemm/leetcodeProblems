def monkeyMove(n):
#        return (2**n - 2) % (10**9+7)
#        return( pow(2,n) -2) % (pow(10,9)+7)
        x = pow(10,9)+7
        return( pow(2,n,x) -2) % x
        """
        :type n: int
        :rtype: int
        """


print("-----")
print(monkeyMove(3))
print(monkeyMove(4))
#print(monkeyMove(500000003))
#print(monkeyMove(599161385))

