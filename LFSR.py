
import math

init_vector = [1,1,1,1,1,1]

cur_vector = init_vector

table = []

key = ""

temp = [0, 0, 0, 0, 0, 0]

for _ in range(31):
    table.append(cur_vector)
    # print("current vector: ",  cur_vector)
    for i in range(len(cur_vector)-1):
        temp[i+1] = cur_vector[i]
        if i == 0:
            temp[0] = int(math.fmod(cur_vector[-2] + cur_vector[-1], 2))
        elif (i == len(cur_vector)-2):
            key += str(cur_vector[-1])
            break
    print(temp)
    cur_vector = temp.copy()

print(key)
print(table)
