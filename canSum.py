
def canSum(target, numbers, map={}):
    if target in map: return map[target]
    if target==0: return True
    if target<0: return False
    
    for i in numbers:
        remainder = target-i
        if canSum(remainder, numbers, map) == True:
            return True
    
    map[target] = False
    return map[target]
        
print(canSum(7, [2, 3]), flush=True)
print(canSum(7, [5, 3, 4, 7]), flush=True)
print(canSum(7, [2, 4]), flush=True)
print(canSum(8, [2, 3, 5]), flush=True)
print(canSum(300, [7,14]), flush=True)
        
    