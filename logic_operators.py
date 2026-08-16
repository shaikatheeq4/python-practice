weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    convert = float(weight) * 0.45
    print(f"You are {convert} kilos")
else:
    convert = float(weight) // 0.45
    print(f"You are {convert} pounds")