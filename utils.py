#Largest no. in a list
def find_max(numbers):
    max = numbers[0]
    for x in numbers:
        if x>max:
            max = x
    return max

