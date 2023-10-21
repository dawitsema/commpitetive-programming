def can_erase_string(s):
    count_A = s.count('A')
    count_B = s.count('B')
    count_C = s.count('C')

    return (count_A + count_B) % 2 == 0 and (count_B + count_C) % 2 == 0

t = int(input())

for _ in range(t):
    s = input()  
    result = can_erase_string(s)
    
    if result:
        print("YES")
    else:
        print("NO")
