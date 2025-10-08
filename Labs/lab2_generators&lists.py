

## PROBLEM 1 --------------------------------------------------------------
def between(*variables):
    if len(variables) == 1:
        value = variables[0]
        low = 0.0
        high = 0.3
    elif len(variables) == 2:
        value = variables[0]
        low = variables[1]
        high = 0.3
    elif len(variables) == 3:
        value = variables[0]
        low = variables[1]
        high = variables[2]
    else:
        raise ValueError(f"Received {len(variables)} arguments, expected 1, 2, or 3.")
    if low <= value <= high:
        return True
    else:
        return False

print('One variable between', between(0.2))
print('One variable outside', between(0.4))
print('Two variables between', between(0.2, 0.1))
print('Two variables outside', between(0.0, 0.1))
print('Three variables between', between(0.4, 0.1, 5.0))
print('Three variables outside', between(0.0, 0.1, 5.0))


## PROBLEM 2 --------------------------------------------------------------
def rangef(max,step):
    value = 0.0
    while value <= max:
        yield value
        value += step

for i in rangef(5,0.5): print(i, end=' ')
print('')


## PROBLEM 3 --------------------------------------------------------------
alist = []
for i in rangef(1,0.25):
    alist.append(i)
print(alist)

blist = alist[::-1]             # reverses a python list
blist = reversed(alist)         # reverses a python list
for i in blist:
    alist.append(i)
print(alist)

sortedlist = sorted(alist)
sortedlist.sort(key=between, reverse=False)
print(sortedlist)


## PROBLEM 4 --------------------------------------------------------------
list = [x for x in range(16) if x%2==0 or x%3==0]
print(list)