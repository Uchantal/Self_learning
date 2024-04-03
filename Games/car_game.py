command = ""
started = False

while True:
    command = input(">").lower()

    if command == "start":
        if started:
            print("A car has already started")
        else:
            started = True
            print("Car has started")
    
    elif command == "stop":
        if not started:
            print("It has already stopped")
        else:
            started = False
            print('It has stopped')

    elif command == "help":
        print("""
start - to start a car
stop - to stop a car
quit - to quit
""")

    elif command == "quit":
        break

    else:
        print("I don't know that")



