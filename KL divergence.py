import math
p = [0.36, 0.48, 0.16]
q = [0.333, 0.333, 0.333]

sum = 0
for i in range(len(p)):
    sum += p[i] * math.log(p[i]/q[i])

print(sum)

sum2 = 0
for i in range(len(p)):
    sum2 += q[i] * math.log(q[i]/p[i])

print(sum2)
