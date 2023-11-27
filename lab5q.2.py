# Input: Take a positive number N
while True:
    try:
        N = int(input("Enter a positive number N: "))
        if N > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Display numbers not divisible by N in the range 1-1000
number = 1
while number <= 1000:
    if number % N == 0:
        number += 1
        continue
    print(number)
    number += 1
