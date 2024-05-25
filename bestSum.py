def bestSum(target, num, map={}):
    if target in map: return map[target]
    if target==0: return []
    if target<0: return None
    
    shortest = None
    
    for i in num:
        remainder = target - i
        arrBest = bestSum(remainder, num)

        if(arrBest != None):
            arr = arrBest + [i]
            if(shortest == None or len(arr) < len(shortest)):
                shortest = arr
            
    map[target] = shortest
    return map[target]

print(bestSum(40,[10,2,3,4,5,6,7,8,9,1]))  