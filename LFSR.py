
import math

init_vector = [1,1,1,1,1,1]

cur_vector = init_vector

table = []

key = ""

temp = [0, 0, 0, 0, 0, 0]

for _ in range(3):
    table.append(cur_vector)
    print(table)
    for i in range(len(cur_vector)):
        if(i == 0):
            n = cur_vector[-2] + cur_vector[-1]
            print(n)
            temp[0] = int(math.fmod(n, 2))
        elif(i == len(cur_vector)-1):
            key += str(cur_vector[i])
            break
        temp[i+1] = cur_vector[i]
    temp = [0, 0, 0, 0, 0]
    # print(temp)
    cur_vector = temp

print(table)
