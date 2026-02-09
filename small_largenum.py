largest = None
smallest = None

while True:
    num_input = input("Enter a number: ")
    
    if num_input == 'done':
        break
        
    try:
        num = int(num_input)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num
        
    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
