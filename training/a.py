from ctypes import c_int as c, addressof as ad

a = [1, 2, 3, 4, 5] 
b = (1, 2, 3, 4, 5) 
c = {1, 2, 3, 4, 5}
d = {'a' : 1, 'b' : 2} 

print(hex(id(a[0])))

for i in a:
    print(hex(id(i)) + " ", end="")
    
print("")

for i in b:
    print(hex(id(i)) + " ", end="")
    
print("")

for i in c:
    print(hex(id(i)) + " ", end="")
