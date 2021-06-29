def areRotations(string1, string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = ''
    if size1 != size2: 
        return False
    temp = string1 + string1
    if (temp.count(string2)> 0): 
        return True
    return False

string1 = "AACD"
string2 = "ACDA"
print(areRotations(string1, string2))