
def print_pyramid(N):
    
    for i in range(1, N + 1):

        stars = 2 * i - 1
        
        spaces = N - i
        
        print(' ' * spaces + '*' * stars)


N = int(input("Enter the value of N: "))
print_pyramid(N)
