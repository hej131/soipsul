import random
array = []

for i in range(100):
    i = random.randint(1,1000)
    array.append(i)

print array

max = 0

for i in range(100):
    if array[i]>max:
        max = array[i]

print 'Maximum number is ' + str(max)

