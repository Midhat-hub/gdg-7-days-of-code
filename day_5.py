
n = int(input("Enter the size of array: "))

mylist = list(map(int, input("Enter the array elements: ").split()))

sum = 0

for i in mylist:
    if i > 0:
        sum += i

print(sum)
