a = int(input())
b = int(input())

def grid(a,b, map={}):
    if(b>a):
        temp = a
        a = b
        b = temp
        
    key = str(a) + ',' + str(b)
    
    if(key in map):
        return map[key]
    if a==1 and b==1: return 1
    if a==0 or b==0: return 0
    map[key] = grid(a-1,b) + grid(a,b-1)
    return map[key]

print(grid(a,b))

