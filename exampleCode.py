# No spaces between characters
for x in "enme441":
    print(x, end="")

print()  # for newline
# Space between characters
for x in "enme441":
    print(x, end=" ")


print()  # for newline
while True:
    try:
        val = int(input("Enter a value: "))
        with open('data.txt', 'r') as f:
            for line in f:
                if int(line) > val:
                    print(line.strip())
    except:
        print('must enter a numerical value')