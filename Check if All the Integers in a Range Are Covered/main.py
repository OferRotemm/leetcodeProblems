def isCovered(ranges, left, right):
        l = left

        def my_sort(sub_list):
            return sub_list[0]
        
        rg = sorted(ranges, key=my_sort)

        while right >= l:
                for i in rg:
                        if i[0] < l:
                                    if i[1] == l:
                                            if i[1] >= right:
                                                    return True
                                            l += 1
                                    elif i[1] > l:
                                            if i[1] >= right:
                                                    return True
                                            l = i[1] + 1
                        elif  i[0] == l:
                                if l == right:
                                        return True
                                l += 1
                                if i[1] < l: continue
                                elif i[1] == l:
                                        l += 1
                                elif i[1] > l:
                                        if right <= i[1]:
                                                return True
                                else: return False
                return False
        return "error"


w = [[1,2],[3,4], [5,6]]
x = [[1,10],[10,20]]
y = [[1,10],[30,40]]
z = [[1,20],[25,40]]
v = [[1,2],[10,20]]
u = [[10,20],[1,10]]
t = [[1,5],[3,15],[14,20]]
q = [[23,43],[12,17],[14,35],[13,20],[16,24],[6,18],[6,49],[6,29],[37,42],[22,42],[15,25],[3,20],[12,21],[21,38],[16,20],[7,22],[35,40],[38,39],[6,16],[2,15],[16,26],[5,18],[5,36],[5,47],[2,41],[1,19],[23,49],[31,32],[7,10],[33,50],[5,21],[33,43],[12,12],[10,50],[10,21],[7,20],[33,46],[19,39],[9,14],[10,35],[3,47]]
r = [[36,50],[14,28],[4,31],[24,37],[13,36],[27,33],[23,32],[23,27],[1,35]]
s = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13],[14,14],[15,15],[16,16],[17,17],[18,18],[19,19],[20,20],[21,21],[22,22],[23,23],[24,24],[25,25],[26,26],[27,27],[28,28],[29,29],[30,30],[31,31],[32,32],[33,33],[34,34],[35,35],[36,36],[37,37],[38,38],[39,39],[40,40],[41,41],[42,42],[43,43],[44,44],[45,45],[46,46],[47,47],[48,48],[49,49]]


print("-------")
print("1 expected: True \n result:")
print(isCovered(w,2,5))
print("-------")
print("2 expected: False \n result:")
print(isCovered(x,21,21))
print("-------")
print("3 expected: False \n result:")
print(isCovered(y,8,18))
print("-------")
print("4 expected: True \n result:")
print(isCovered(z,25,40))
print("-------")
print("5 expected: False \n result:")
print(isCovered(v,9,15))
print("-------")
print("6 expected: error \n result:")
print(isCovered(v,20,15))
print("-------")
print("7 expected: True \n result:")
print(isCovered(u,8,12))
print("-------")
print("8 expected: True \n result:")
print(isCovered(t,8,12))
print("-------")
print("9 expected: True \n result:")
print(isCovered(s,1,49))
print("-------")
print("10 expected: True \n result:")
print(isCovered(r,35,40))
print("-------")
print("11 expected: True \n result:")
print(isCovered(q,21,50))
print("-------")

                
"""
:type ranges: List[List[int]]
:type left: int
:type right: int
:rtype: bool
"""
