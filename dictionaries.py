phone= (input("phone: "))
list1= {
    "1" : "one",
    "2" : "Two",
    "3" : "three",
    "4" : "four"
}
op= ""
for n in  phone:
    op += list1.get(n,"!") + " "
print(op)
