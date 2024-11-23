
def count_vowels(string):
    
    vowels = set("aeiouAEIOU")
    
    count = 0
    
    for char in string:
    
        if char in vowels:
            count += 1
    return count


input_string = input("Enter the string: ")

result = count_vowels(input_string)
print(result)
