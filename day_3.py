x=int(input())
y=int(input())
if x >= y:
    print("Error: The first number must be less than the second.")
    exit()
if x < 0 or y < 0:
    print("Error: Both numbers must be non-negative.")
    exit()
for i in range(x,y+1):

    if i%5==0 and i%7==0:
        print("FooBar")
    elif i%5==0 and i%7!=0:
        print("Foo")    
    elif i%5!=0 and i%7==0:
        print("Bar")  
    else:
        print("Baz")      
        