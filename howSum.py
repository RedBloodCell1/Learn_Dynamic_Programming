def howSum(target, num=[], map={}):
    if(target in map):
        return None
    if target==0: return []
    if target<0: return None
    
    for i in num:
        rem = target-i
        
        ans = howSum(rem, num, map)
        if(ans != None):
            return ans + [i]
        else:
            map[target] = None

print(howSum(7,[3,1]))

    