
n, t = input().split()
n = int(n)
t = int(t)

s = []
d = []

for i in range(n):
    left, right = input().split()
    s.append(int(left))
    d.append(int(right))

while True:

    for i in range(n):
        while s[i] < t:
            s[i] += d[i]

    if t in s:
        print(s.index(t) + 1)
        break
    
    t += 1