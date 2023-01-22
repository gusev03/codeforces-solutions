
entries = int(input())
inputs = []

for i in range(entries):
    inputs.append(input())

for i in inputs:
    length = len(i)
    if length > 10:
        print(i[0] + str(length - 2) + i[length - 1])
    else:
        print(i)