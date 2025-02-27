print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("you are eligible to ride")
    age = int(input("What is your Age in years? "))
    if age >= 18:
        bill = 12
        print("ticket is 12 dollars")
    elif age < 18 and age >= 12:
        bill = 7
        print("ticket is 7 dollars")
    elif age < 12:
        bill = 5
        print("ticket is 5 dollars")

    want_photo = input("Do you want your photo to be taken at ride which will cost you $3 press 'y' to YES 'n' to NO ")
    if want_photo == "y":
        bill += 3

    print(f"you total bill is ${bill}")
else:
    print("you are not eligible to ride")

