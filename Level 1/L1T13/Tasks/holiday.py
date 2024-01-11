# ===== TRAVEL PLANNER ====

# User menu for city selction
def city_choice ():
    print("1: Barcelona")
    print("2: Lisbon")
    print("3: Athens")
    print("4: Malta")
    print("5: Cyprus")
    print("6: Exit")
    print()

# Calculates hotel cost
def hotel_cost (num_nights, price):
    cost_hotel = round(num_nights * price)
    return (cost_hotel)

# Calculates plane cost
def plane_cost (city_flight):
    flight_prices = [90, 110, 220, 190, 260] # List with predefined flight prices for each city
    return (flight_prices[city_flight])

# Calculates car rental price
def car_rental (rental_days, city_flight):
    rental_prices = [60, 55, 50, 50, 45]  # List with pre-defined car rental prices
    car_price = round(rental_days * rental_prices[city_flight])
    return (car_price)

# Calculates total price of holiday
def holiday_cost (hotel, plane, car):
    total_cost = hotel + plane + car
    return (total_cost)

# Pre-defined cities and prices
city_flight = ['Barcelona', 'Lisbon', 'Athens', 'Malta', 'Cyprus']
hotel_prices = [90, 85, 79, 78, 80]

menu_choice = 0
print("Welcome to the travel planner!")
city_choice ()

while menu_choice != 6:

    menu_choice = int(input("Select the city you want to travel to: "))

    if menu_choice > 0 and menu_choice < 6:
        num_nights = int(input("How many nights are you staying? "))
        rental_days = int(input("How many days do you want to rent a car for? "))
        print()
        print(f"Holiday cost breakdown for {num_nights} days in {city_flight[menu_choice-1]} is:")
        print("Hotel cost: £", hotel_cost(num_nights, hotel_prices[menu_choice-1]))
        print("Plane cost: £", plane_cost(menu_choice-1))
        print("Car rental cost: £", car_rental(rental_days, menu_choice-1))
        print("The total cost of your holiday is: £", holiday_cost(hotel_cost(num_nights, hotel_prices[menu_choice-1]), plane_cost(menu_choice-1), car_rental(rental_days, menu_choice-1)))
        menu_choice = 6 # force exit menu

    elif menu_choice == 6:
        print("See you soon!")

    else:
        print("Wrong choice, please try again:\n")
        city_choice ()

