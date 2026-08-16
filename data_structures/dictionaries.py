phone = input("Phone: ")

number_words = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}

output = ""
for digit in phone:
    output += number_words.get(digit, "!") + " "

print(output)
