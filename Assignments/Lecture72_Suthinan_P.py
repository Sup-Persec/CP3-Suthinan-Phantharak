menulist = []

def Bill():
    total = 0
    print("Menu bill".center(21,'-'))
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        total += menulist[number][1]
    print("Total price :", total)
    print('-'*21)

while True:
    menuName = input("Please enter menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menulist.append([menuName,menuPrice])

Bill()