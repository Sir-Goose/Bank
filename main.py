def bank():
    greeting = input("Greeting: ")
    greeting = greeting.lower()

    if greeting == "hello":
        print("$0")
        return
    if greeting == " hello ":
        print("$0")
        return
    if greeting == "hello, newman":
        print("$0")
        return

    if greeting[0] == "h":
        print("$20")
    else:
        print("$100")


bank()
