started = False

while True:
    command = input("Enter a command (type 'exit' to quit): ").lower()

    if command == "start":
        if not started:
            print("car started...Ready to go!")
            started = True
        else:
            print("car is already started!")

    elif command == "stop":
        if started:
            print("car stopped")
            started = False
        else:
            print("car is already stopped!")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
help - to display this help message
exit - to quit the program
""")

    elif command == "exit":
        print("Exiting the program...")
        break

    else:
        print("I don't understand that...")