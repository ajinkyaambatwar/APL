import math
n=list()
n.append(0.2)
a=math.pi
for k in range(1,1000):
    num = (n[k-1]+a)*100
    n.append(num-int(num))

for i in range(0,1000):
    n[i] = "{:.4f}".format(n[i])

print(n)
print(len(n))
