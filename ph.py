import re
# Read the number of test cases
N = int(input("enter the ph.no:"))

for _ in range(N):
    phone = input()
    if re.match(r'^[7-9]\d{9}$', phone):
        print("YES")
    else:
        print("NO")
