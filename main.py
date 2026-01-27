# Game "try to not divide by 2"
x = int(input("Enter your num: "))
while x % 2 == 0:
    print("U lose!")
    x = int(input("Enter ypur num:"))
print("U win!")