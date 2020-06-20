systemMenu = {"ข้าวมันไก่":40,"ข้าวมันไก่":45,"ข้าวมันไก่ผสม":50}
menulist = []

def Bill():
    total = 0
    print("Menu bill".center(21,'-'))
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1],"THB")
        total += menulist[number][1]
    print("Total price :", total,"THB")
    print('-'*21)

while True:
    menuName = input("Please enter menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menulist.append([menuName,systemMenu[menuName]])

Bill()