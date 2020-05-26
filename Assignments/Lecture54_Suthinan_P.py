def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("Wrong Username or Password")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Result :", vatCal(int(input("Price : "))))
    elif userSelected == 2:
        print("Result :", priceCal())
    else:
        print("Please select again.")
        return menuSelect()
def vatCal(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCal(price1 + price2)

login()
showMenu()
menuSelect()
