def maximumSubarraySum(nums, k):
        maxSum = None
        itmInLoop = None
        for itm in nums:
                if itmInLoop == None:
                        itmInLoop = 0
                else:
                       itmInLoop += 1
                def maxCheck(start, end):
                        nSum = sum(nums[start:end])
                        if maxSum != None:
                            if nSum > maxSum:
                                    return nSum
                            else:
                                    return maxSum
                        else:
                               return nSum
                if itmInLoop > nums.index(itm):
                       continue
                starts = [i for i, x in enumerate(nums) if x == itm]
                ends = [i for i, x in enumerate(nums) if x == itm-k or x == itm+k]
                staresI = 0
                endsI = 0
                tempSum = None
                tempSumS = None
                tempSumE = None
                while True:
                        if starts[staresI+1] < ends[endsI]:
                                tempSum1 = sum(nums[staresI:staresI+1])
                                staresI += 1
                                if tempSumS == None:
                                        tempSumS = tempSum1
                                elif tempSum1 > tempSumS:
                                       tempSumS = tempSum1
                        elif starts[staresI] < ends[endsI]:
                               tempSum2 = sum(nums[staresI:endsI])
                               staresI += 1
                               endsI += 1
                        elif starts[staresI+1] > ends[endsI+1]:
                               tempSum3 = sum(nums[endsI+:endsI+1]) #####
                        staresI += 1
                        
                        staresI = 

        if maxSum == None:
               return 0
        else:
               return maxSum
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
w = [5,3,2,5,8,10,15,5,5,10,25,-3687,5,2,21,5,36,7,5,10,3,3,54,10]
x = 5

a = [1,2,3,4,5,6] #11
b = 1

c = [-1,3,2,4,5]#11
d = 3

e = [-1,-2,-3,-4]#-6
f = 2

g = [1,230,5554,5]#0
h = 3

i = [1,230,5554,5]#5790
j = 4

k = [201,202,203,503,560,558,6,4,2,0,150,151]#1118
l = 2

m = [-8,580,-6258,7,-7,-6,4789552,36,-9,-7]#4789566
n = 1

o = [1,2,2,2,3,2,2,2]#16
p = 1

q =[3,3,3,6,9,12,-12864,12]#21
r = 3

s = [-636,-784,-356,-832,-797,-978,-651,-667,-907,-900,-168,-697,-879,-998,-126,-900,-542,-553,-268,-374,-710,-768,-727,-975,-106,-756,-462,-815,-276,-163,-301,-822,-367,-685,-581,-488,-763,-612,-847,-730,-479,-874,-221,-912,-229,-543,-876,-845,-424,-215,-819,-164,-840,-525,-987,-291,-658,-168,-382,-781,-951,-396,-228,-394,-445,-863,-290,-675,-289,-950,-885,-228,-624,-236,-437,-246,-302,-741,-243,-419,-851,-980,-667,-661,-140,-893,-328,-354,-359,-845,-396,-309,-450,-941,-310,-119,-614,-854,-599,-605]
t = 8 #-1088

u = [10,-3,-5,7,-4,-10,-8,0,-1,1,9,-3,6,-9,-4,-10,3,0,-6,-6,10,6,-8,6,2,-8,-8,-2,-1,10,5,-8,-3,-2,10,1,5,0,1,6,-9,-5,-6,-4,-8,9,-8,-10,-1,-10,10,5,-2,10,-9,-10,-2,-6,-10,-9,-3,-4,4,-3,0,-4,-1,9,-9,1,1,8,-4,8,-2,4,-7,8,8,5,7,5,10,-3,-5,-4,10,5,5,-1,5,9,-7,7,-6,3,1,10,-10,7,3,0,2,1,3,-10,5,4,-8,2,1,5,0,9,1,5,-7,0,0,-6,-1,5,4,6,0,-8,2,-10,5,7,-5,-5,0,1,-10,-1,8,-3,6,10,8,-8,8,-6,8,0,-3,-4,1,6,2,-1,-10,-4,6,3,10,9,7,-10,6,-6,-3,9,8,-9,-7,-7,-7,-3,-4,8,-10,-9,-3,-7,-8,-10,5,-10,0,10,1,-3,-9,5,8,0,-6,8,4,-10,-4,5,2,1,8,-3,8,-9,7,8,-6,5,-9,-1,-9,9,-9,-4,0,10,5,-10,-8,9,-9,-10,10,-2,-7,7,-1,8,8,4,-1,9,-6,1,8,-10,-8,0,6,-1,-3,-9,6,-1,-3,2,-6,10,9,0,-6,8,1,-10,0,-3,-4,-4,-4,-6,9,-10,-1,-9,-5,-9,-6,-8,-8,7,3,-8,8,-3,-7,-2,-9,7,1,1,-5,-1,5,3,3,-7,5,5,-2,-2,6,8,3,-7,-6,-7,6,6,-5,-4,8,9,-1,-3,-7,6,-2,0,-10,8,6,2,6,8,-10,4,5,-10,-1,-5,0,3,-2,4,6,4,-10,7,2,-7,6,2,4,-1,1,0,1,10,7,-6,-3,-3,-7,9,9,9,10,-10,5,-6,-6,-2,-10,-2,8,8,-5,-3,-9,8,10,-1,-3,-5,1,-4,-9,6,10,6,0,-9,7,7,9,-9,-2,3,7,-6,-5,1,0,-6,-6,-1,-1,-5,-8,-3,-7,-6,-7,9,-8,-8,6,5,9,-4,2,-10,-3,-8,1,-4,-2,-7,10,0,-1,4,-5,-6,10,0,10,-8,8,-3,6,1,-6,-4,-4,-6,-9,3,3,5,5,-1,10,-10,3,10,-2,-10,-10,7,0,10,-4,0,-7,6,8,-5,10,3,-1,6,-9,2,6,4,-6,4,-3,-3,-1,10,-4,-3,1,-9,4,-2,1,3,6,0,0,2,-8,7,2,-6,10,8,5,2,7,10,9,-1,-5,-8,4,3,6,3,7,-5,-3,3,0,-2,-4,-10,-3,1,-8,7,10,-8,0,9,10,-10,9,-2,-7,10,8,-4,-10,8,5,5,-7,-8,0,0,-8,5,0,3,-7,6,3,1,-1,-4,3,4,-9,-9,-8,-1,9,3,-9,2,-6,7,-9,4,8,-9,-4,-2,9,9,-3,-1,8,-10,-7,9,3,-9,-1,-6,7,1,-1,-10,2,-10,0,6,-9,-10,-4,-4,-9,8,0,7,-7,-9,5,-6,9,-7,9,-9,2,2,0,0,6,-8,-2,-6,2,4,5,-3,-8,8,8,5,5,5,1,2,3,-8,5,7,9,10,9,0,1,-1,-1,9,-5,6,-8,-10,-9,6,1,-6,6,-9,-8,8,-2,-3,-2,-8,9,0,5,-4,0,1,6,-7,5,-1,0,10,4,-2,-3,10,-8,8,2,-1,-9,-6,-4,3,8,6,2,7,2,10,9,8,-5,0,-5,7,-1,5,5,6,4,0,1,-10,2,-1,5,0,-1,6,-1,5,-10,-7,-2,7,-6,-7,2,0,8,7,-3,7,-1,-8,1,10,6,9,-7,9,8,-1,-6,3,-6,5,2,-1,9,-7,8,3,-8,1,9,3,-5,-10,4,8,-8,2,10,7,-2,7,4,-8,10,1,-1,-1,-4,-4,-3,-7,-7,8,-6,7,3,-1,-1,4,-2,-6,-9,7,7,2,-1,10,0,5,1,-4,-4,1,-7,4,6,10,-5,-7,6,-2,-7,6,-4,6,5,7,-7,-3,-4,-1,-4,-3,4,-8,2,9,-3,1,-4,8,8,5,-8,9,-5,7,6,6,4,-1,6,8,-6,-2,6,-8,-3,-2,-1,4,3,-4,-7,8,5,-5,-9,8,-5,3,-3,-5,-1,8,9,10,-9,8,-8,3,2,-3,-6,9,-2,10,-6,-1,2,-4,-9,-1,-5,0,0,3,-10,-3,-6,-7,1,5,8,-7,-6,-5,-4,10,-6,-3,-10,9,1,7,-9,-3,-5,-7,-10,-9,-1,-10,-7,6,-10,-10,10,-2,2,-10,-4,-10,4,1,1,-3,-8,-6,4,-1,6,-2,-5,10,10,7,1,-10,9,-3,8,-8,-1,-8,8,-3,-7,-9,5,3,-10,6,-8,-8,4,-10,-9,8,3,3,5,-3,5,-3,0,5,8,10,6,4,5,2,0,0,-8,7,10,3,-7,9,-7,2,4,-1,-4,3,6,3,4,-2,-1,-3,3,8,-5,5,9,10,6,-8,-5,-1,4,10,8,-10,-3,3,7,10,-10,-2,-1,7,-10,3,-6,-6,9,10,3,1,-4,-4,-5,5,7,2,-2,6,7,-5,-9,-7,-4,0,-3,-5,5,-9]
v = 3 #247

print("-------------")
print(maximumSubarraySum(a, b))
print(maximumSubarraySum(c, d))
print(maximumSubarraySum(e, f))
print(maximumSubarraySum(g, h))
print(maximumSubarraySum(i, j))
print(maximumSubarraySum(k, l))
print(maximumSubarraySum(m, n))
print(maximumSubarraySum(o, p))
print(maximumSubarraySum(q, r))
print(maximumSubarraySum(s, t))
print(maximumSubarraySum(u, v))
print("-------------")