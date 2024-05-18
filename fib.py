a = int(input())

def fib(x, map={}):
    if x in map: return map[x]
    if x<=2: return 1
    
    map[x] = fib(x-2, map)+fib(x-1, map)
    return map[x]

print(fib(a))