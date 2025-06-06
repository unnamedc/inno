n = int(input())
x, y, z = list(map(int, input().split()))
 
all_time = 2*(n*x + n*y + n*z)
 
pos_one = [0]*all_time
pos_two = [0]*all_time
pos_three = [0]*all_time
 
 
count_first = 0
first_timer = 0
 
count_two = 0
two_timer = 0
flag_two = False
 
count_three = 0
three_timer = 0
flag_three = False
 
 
if x >= y:
    for i in range(all_time):
        pos_one[i] += count_first
        pos_two[i] += count_two
        pos_three[i] += count_three
 
 
        first_timer += 1
        if first_timer == x:
            first_timer = 0
            count_first += 1
 
        if pos_two[i] > 0 and pos_one[i] > 0:
            flag_three = True
            count_two -= 1
            count_first -= 1
            pos_one[i] -= 1
            pos_two[i] -= 1
 
        if pos_one[i] > 0:
            flag_two = True 
            count_first -= 1
            pos_one[i] -= 1
 
 
 
        if flag_three:
            three_timer += 1
            if three_timer == z:
                three_timer = 0
                count_three += 1
                flag_three = False
 
 
        if flag_two:
            two_timer += 1
            if two_timer == y:
                two_timer = 0
                count_two += 1
                flag_two = False
                
        if count_three >= n:
            print(i + 1)
            break
 
else:
    for i in range(all_time):
        pos_one[i] += count_first
        pos_two[i] += count_two
        pos_three[i] += count_three
 
 
        first_timer += 1
        if first_timer == x:
            first_timer = 0
            count_first += 1
 
 
        if pos_one[i] > 0:
            two_timer += 1
            if two_timer == y:
                two_timer = 0
                count_two += 1
                flag_two = False
                count_first -= 1
 
        if pos_two[i] > 0 and pos_one[i] > 0:
            three_timer += 1
            if three_timer == z:
                three_timer = 0
                count_three += 1
                flag_three = False
                count_first -= 1
                count_two -= 1
                
        if count_three >= n:
            print(i + 1)
            break
