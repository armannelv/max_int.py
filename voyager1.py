# Þetta forrit reiknar og skrifar út upplýsingar fyrir fyrirtæki sem leigir bíla til viðskiptavina sinna.
# Forritið reiknar út upphæð sem viðskiptavinur þarf að greiða og byggir útreikningurinn á viðskiptavinakóða
# fjölda daga yfir leigutímabilið og fjölda mílna sem keyrðir voru.

print("Welcome to car rentals!")

budget_code = 40
budget_milage = 0.25
daily_code = 60
daily_miliage = 0.25

# while loopa
# "Miles driven: "
# "Amount due: "


car_rentals_program = True

while car_rentals_program == True:

    prompt_user = str(input("Would you like to continue (y/n)? "))

    if prompt_user == "n":
        car_rentals_program = False
        # break

    customer_code = str(input("Customer code (b or d): "))
    num_days = int(input("Number of days: "))
    odom_start = int(input("Odometer reading at the stort: "))
    odom_end = int(input("Odometer reading at the end: "))

    miles_driven = odom_end - odom_start

    budget_amount = (num_days * budget_code) + (miles_driven * budget_milage)

    daily_amount = (num_days * daily_code) + ((miles_driven - 100) * daily_miliage)

    if customer_code == "b":
        print("Miles driven: ", miles_driven)
        print("Amount due: ", budget_amount)

    elif customer_code == "d":

        if miles_driven <= 100:
            under_one_hundred = (num_days * daily_code)
            print("Miles driven: ", miles_driven)
            print("Amount due: ", under_one_hundred)
        else:
            print("Miles driven: ", miles_driven)
            print("Amount due: ", budget_amount)
