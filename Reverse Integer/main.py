def reverse(x):
        rang = pow(2,31) # 2147483648
        s = str(x)
        if x > 0:
                max = str(rang-1)
                reverse = ""
                if len(s) < len(max):
                        for i in range(1,len(s)+1):
                            reverse += s[-i]
                        return 0 + int(reverse) 
                else:
                    for i in range(1,len(s)+1):
                            if s[-i] > max[i-1]:
                                    return 0
                            elif s[-i] == max[i-1]:
                                   reverse += s[-i]
                            else:
                                for x in range(i,len(s)+1):
                                                    reverse += s[-x]
                                return 0 + int(reverse)         
                    return 0 + int(reverse)
        elif x < 0:
                s = s[1:]
                min = str(rang)
                reverse = "-"
                if len(s) < len(min):
                        for i in range(1,len(s)+1):
                            reverse += s[-i]
                        return 0 + int(reverse) 
                else:
                    for i in range(1,len(s)+1):
                            if s[-i] > min[i-1]:
                                    return 0
                            elif s[-i] == min[i-1]:
                                   reverse += s[-i]
                            else:
                                for x in range(i,len(s)+1):
                                                    reverse += s[-x]
                                return 0 + int(reverse)         
                    return 0 + int(reverse)       
        else: return 0
        """
        :type x: int
        :rtype: int

        """

print("----------")
print(reverse(123)) #321
print(reverse(-123)) #-321
print(reverse(12300)) #321
print(reverse(-12300)) #-321
print(reverse(-2147483648)) #0   
print(reverse(2147483647)) #0
print(reverse(0)) #0
print(reverse(1111111512)) #0
print(reverse(-2147483412)) #-2143847412
print("----------")