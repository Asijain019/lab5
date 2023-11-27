# Input: Take a positive integer N
while True:
    try:
        N = int(input("Enter a positive integer N: "))
        if N > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Initialize counters
divisible_count = 0
not_divisible_count = 0

# Take numbers from the user until -999 is entered
while True:
    num = int(input("Enter a number (enter -999 to stop): "))
    
    # Check if the user entered -999 to stop
    if num == -999:
        break
    
    # Check if the number is divisible by N
    if num % N == 0:
        divisible_count += 1
    else:
        not_divisible_count += 1

# Display the counts
print(f"Count of numbers divisible by {N}: {divisible_count}")
print(f"Count of numbers not divisible by {N}: {not_divisible_count}")
