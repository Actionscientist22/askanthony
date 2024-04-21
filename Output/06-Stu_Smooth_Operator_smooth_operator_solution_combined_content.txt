# Declare variables
budget = 2000
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]
days = input("How many days can you travel? ")
city_to_visit = input("What city would you like to visit? ")

# Check if days is a number, and convert it to an integer if it is
if days.isdigit():
    days = int(days)
# Else print an error
else:
    print("Input was not a number.")

# Check if budget and days are integers, and if so, calculate the daily budget
if type(days) is int and type(budget) is int:
    daily_budget = budget / days
    print(f"The daily budget is ${daily_budget}")
# Else print an error
else:
    print("There was an error. Unable to calculate daily budget.")

# Check if the city_to_visit is in the cities list
if city_to_visit in cities:
    # Get the daily cost for the city
    city_index = cities.index(city_to_visit)
    city_daily_cost = cities_daily_cost[city_index]
# Else set the city_daily_cost to 0 to be used for error checking
else:
    city_daily_cost = 0

# Check if the city_daily_cost is greater than 0 and equal to or less than
# the daily budget
if city_daily_cost > 0 and city_daily_cost <= daily_budget:
    # Tell the traveler they can afford the vacation
    print(
        f"You can afford the trip to {city_to_visit} for {days} days with "
        + f"your daily budget of ${daily_budget} because the daily cost is $"
        + str(city_daily_cost)
    )
# Else if the city_daily_cost is greater than 0 and greater than the daily
# budget
elif city_daily_cost > 0 and city_daily_cost > daily_budget:
    # Calculate and print out how much more per day the traveler needs
    need_daily = city_daily_cost - daily_budget
    print(
        f"You'll have to wait to travel when you can afford ${need_daily} "
        + "more per day."
    )
# Else print an error
else:
    print("City was not in list. We cannot make any recommendations.")
