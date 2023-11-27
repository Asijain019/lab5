# Input: Take a positive integer N between 1 and 20
while True:
    try:
        N = int(input("Enter a positive integer N between 1 and 20: "))
        if 1 <= N <= 20:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Display multiplication tables
for i in range(1, N + 1):
    for j in range(1, 21):
        result = i * j
        print(f"{i} x {j} = {result}")
