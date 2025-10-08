# FOR Loop
x = 0.5
sum = 0.0
for k in range(1, 6):
    sum += (((-1)**(k-1))*((x-1)**k))/k
s1 = "f(0.5) ~= {:.9f} with {:d} terms".format(sum, k)
print(s1)

# WHILE Loop
x = 0.5
sum = 0.0
newValue = 1
k = 1
while abs(newValue) >= 10**-7:
    newValue = (((-1)**(k-1))*((x-1)**k))/k
    sum += newValue
    k += 1
s2 = "f(0.5) ~= {:.9f} with {:d} terms".format(sum, k)
print(s2)