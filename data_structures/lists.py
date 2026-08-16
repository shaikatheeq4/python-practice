def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [2, 11, 12, 3, 4, 5]
print(find_max(numbers))
