def vatcal(totalprice):
    result = totalprice+(totalprice*7/100)
    return result

print(vatcal(int(input(">> "))))