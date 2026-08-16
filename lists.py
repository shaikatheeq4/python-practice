#Largest no. in a list
def find_max():

    numbers= input("Give any list with numbers:")
    max = numbers[0]
    for x in numbers:
        if x>max:
            max = x
    print(max)
find_max()    

    

