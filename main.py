print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Kids ticket is $5.")
        bill = 5
    elif age <= 18:
        print("Youth ticket is $7.")
        bill = 7
    elif 45 <= age <= 55:
        print("You get a free ticket! Things will be Alright!")
        bill = 0
    else:
        print("Adult ticket is $12.")
        bill = 12
    want_photo = input ("Do you want a photo to be taken? type Y for yes or N for no")
    if want_photo == "Y":
        bill += 3
    print(f"Your total bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
