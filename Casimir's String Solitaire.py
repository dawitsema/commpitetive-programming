# Define a function to check if the string can be fully erased
def can_erase_string(s):
    # Count the number of 'A', 'B', and 'C' in the string
    count_A = s.count('A')
    count_B = s.count('B')
    count_C = s.count('C')

    # Check if the total count of 'A' and 'B' is even and the total count of 'B' and 'C' is even
    return (count_A + count_B) % 2 == 0 and (count_B + count_C) % 2 == 0

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    s = input()  # Read the input string for this test case
    result = can_erase_string(s)
    
    # Print "YES" if it's possible to fully erase the string, otherwise print "NO"
    if result:
        print("YES")
    else:
        print("NO")
