# Define a function to calculate the minimum number of operations to make two strings equal
def min_operations_to_equal_strings(a, b):
    min_operations = float('inf')  # Initialize with a large value

    # Try all possible combinations of operations on both strings
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            new_a = a[i:] + a[:i]  # Apply operations on string 'a'
            new_b = b[j:] + b[:j]  # Apply operations on string 'b'

            # Calculate the number of operations required to make both strings equal
            operations = i + j + abs(len(new_a) - len(new_b))

            # Update the minimum operations if the current combination is better
            min_operations = min(min_operations, operations)

    return min_operations

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    a = input()  # Read string 'a'
    b = input()  # Read string 'b'
    
    # Calculate and print the minimum number of operations for this test case
    result = min_operations_to_equal_strings(a, b)
    print(result)
