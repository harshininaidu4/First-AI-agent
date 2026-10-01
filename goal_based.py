temp = 100
goal = 72

while temp != goal:
    if temp > goal:
        temp -= 1
    else:
        temp += 1

print("Goal reached:", temp)