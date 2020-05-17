number = int(input("Enter number : "))
space = " "
for i in range(number):
    print(space * (number-i) + "*" * (i*2+1))