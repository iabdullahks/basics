print("Welcome to the Magic Numbers Game!")
print("Guess numbers between 1 and 50. Type 'exit' to quit.")

while True:
    user_input = input("Enter a number: ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Game over!")
        break
    
    # Convert to integer safely
    
    number = int(user_input)
    
    # Skip invalid numbers
    if  number % 4 != 0:
        continue
    
    # If magic number
    
    if number % 4 == 0:
        print("You found a magic number!")
