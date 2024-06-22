def canConstruct(ransomNote, magazine):
    m = list(magazine)
    for i in ransomNote:
        if i in m:
            m.remove(i)
        else: return False
    return True



a = "acab"
b = "abc"

print(canConstruct(b , a))
        