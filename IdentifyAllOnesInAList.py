list = [1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1]

#print(len(list))

Matching_Value = 0

for x in list:
    if x == 1:
        Matching_Value += 1
    if x != 1:
        continue

print(Matching_Value)