#https://www.reddit.com/r/Python/comments/fjqoxv/laid_off_for_8_weeks_anyone_else_starting_their/fkp43bj/

list = [1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1]

#print(len(list))

Matching_Value = 0

for x in list:
    if x == 1:
        Matching_Value += 1
    if x != 1:
        continue

print(Matching_Value)