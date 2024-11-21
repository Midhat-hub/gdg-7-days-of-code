x,y,z= map(int, input("Enter two numbers separated by a space: ").split())

T=x*y

if z > ((T) * 50) / 100:
    print("yes")
else:
    print("no")
