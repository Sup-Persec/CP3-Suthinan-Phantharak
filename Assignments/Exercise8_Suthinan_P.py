userName = input("Username : ")
passWord = input("Password : ")
if userName == "admin" and passWord == "admin":
    print("---Welcome to Shop---")
    print("1.Notebook   200 THB")
    print("2.Macbook    250 THB")
    print("3.IphoneX    150 THB")
    choice = int(input(">>>"))
    if choice == 1 or choice == 2 or choice == 3:
        amount = int(input("Amount\n>>>"))    
        if choice == 1: 
            choice = 200
            print("Total product price :",choice*amount,"THB")
        elif choice == 2: 
            choice = 250
            print("Total product price :",choice*amount,"THB")
        elif choice == 3:
            choice = 150
            print("Total product price :",choice*amount,"THB")
        else:
            print("Error!! Try again later.")
    else:
        print("Product not found!!")
else :
    print("Error!! Invalid username or password.")