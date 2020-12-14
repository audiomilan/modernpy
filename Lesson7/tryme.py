 #Handle exceptions and such.
 #NameError

name = input("Please tell me your name: ")

def introduction():
    try:
        if name == "":
            raise NameError
    except NameError:
        print("im sorry you have to give me something")
        print(f"Missing something Bro")
    finally:
        print(f"Thank you and its a pleasure to meet you: {name}")

def errorMessage():
    print("The shit doesn't work yo!")

try:
     empty_function = "I_am_an_empty_function"
     if empty_function: raise NameError("This thing is empty")

except NameError as e:
    print(e)
    #errorMessage()
else:
    print("All good here! :)")
finally:
    print("We are now free to move on.")

introduction()
