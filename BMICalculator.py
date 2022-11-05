def calculator():
    feet = float(30.48)
    inch = float(2.54)
    pounds = float(0.453592)

    Age = int(input("Enter your age : ")) # Age must be greater than 16 for BMI calculation
    AgeLimit = 16

    if Age < AgeLimit:
        print("This calculation for older than", AgeLimit)
        again()
    else:
        Weight = int(input("Enter weight in pounds : "))
        Feet = int(input("Enter feet : "))
        Inch = int(input("Enter inch : "))

        FeetToCm = Feet * feet
        InchToCm = Inch * inch
        Meter = float(FeetToCm + InchToCm)
        PoundToKg = Weight * pounds
        BMI = PoundToKg / (Meter / 100) ** 2

        if BMI < 18.5:
            print("Your BMI is : ", BMI)
            print("You Are Underweight.")
        elif 18.5 <= BMI <= 24.9:
            print("Your BMI is : ", BMI)
            print("You Are Normal.")
        elif 25.0 <= BMI <= 29.9:
            print("Your BMI is : ", BMI)
            print("You Are Overweight.")
        elif BMI > 30.0:
            print("Your BMI is : ", BMI)
            print("You Are Obese.")


calculator()


def again():
    UserInput = " "
    while True:
        UserInput = input("Do you want to calculate again? (yes/no) : ")
        if UserInput.lower() == "yes":
            print("You selected yes and the calculator starting again...")
            calculator()
        elif UserInput.lower() == "no":
            print("You selected no and the calculator stopped...")
            exit()
        else:
            print("Please only write yes or no.")


again()