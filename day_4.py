n=int(input("Enter number of test cases: "))
for i in range(n):
    x,y,z= map(int, input("Enter three  numbers separated by a space: ").split())

    T=x*y

    if z > ((T) * 50) / 100:
        print("yes")
    else:
        print("no")
