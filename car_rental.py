# This program calculates and writes out information for a car rental.
# It computes amount that the customer has to pay, the calculation depends on what customer code,
# how many day's rented and how many miles the car was driven.

print("Welcome to car rentals!")

# Variables
budget_code = 40
budget_mileage = float(0.25)
daily_code = 60
daily_mileage = float(0.25)

car_rentals_program = True

# The main while loop
while car_rentals_program:

    prompt_user = input("Would you like to continue (y/n)? ")

    if prompt_user == "n":
        car_rentals_program = False
        break
    # Input from user
    customer_code = input("Customer code (b or d): ")
    num_days = int(input("Number of days: "))
    odom_start = int(input("Odometer reading at the start: "))
    odom_end = int(input("Odometer reading at the end: "))

    # Most of the calculation
    miles_driven = odom_end - odom_start

    budget_amount = float((num_days * budget_code) + (miles_driven * budget_mileage))

    free_daily_miles = float(num_days * 100)

    daily_amount = float((num_days * daily_code) + ((miles_driven - free_daily_miles) * daily_mileage))

    # Delivery of information
    if customer_code == "b":
        print("Miles driven:", miles_driven)
        print("Amount due:", float(round(budget_amount, 1)))

    elif customer_code == "d":

        if miles_driven <= 100:
            under_one_hundred = (num_days * daily_code)
            print("Miles driven:", miles_driven)
            print("Amount due:", float(round(under_one_hundred)))
        else:
            print("Miles driven:", miles_driven)
            print("Amount due:", float(daily_amount))
