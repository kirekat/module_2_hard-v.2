import random
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
win = random.choice(numbers)
my_list = []
for i in range (1, win):
    for j in range (i+1, win):
        k = (i + j)
        if win % k == 0 and i != j:
            my_list.append(i)
            my_list.append(j)

print(win)
print(*my_list, sep='')


