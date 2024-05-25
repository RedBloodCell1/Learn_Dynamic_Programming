map = {}

angka = [1,3,3,4,5,2,3,4,1,3,3,4,5,7,8,9,7,6,4,3,3,4,5,7,8,8,6,5,4,3,2,4,6,7,9,0,1]

for i in angka:
    if(i not in map):
        map[i] = [i]
    else:
        map[i].append(i)
        
print(map)
    