# Declare lists
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]

# Loop 3 times through the cities list
for _ in range(3):
    # Ask the user for a city and convert it to title case
    city = input("What city should be added to the list? ").title()
    # Append the city to the cities list
    cities.append(city)

# Use a while loop to append to the cities_daily_cost list as long as that list
# is shorter than the cities list
while len(cities_daily_cost) < len(cities):
    # Use the length of cities_daily_cost for the index of cities to print its
    # value when asking the cost to append to the cities_daily_cost list
    index = len(cities_daily_cost)
    cost = int(input(f"What is the daily cost for {cities[index]} "))
    cities_daily_cost.append(cost)

# Loop through the cities_daily_cost list and add 10 to each item
for i in range(len(cities_daily_cost)):
    cities_daily_cost[i] += 10

# Use a for loop to loop through both of the lists at the same time, since
# they're the same length, and print out the city and daily cost on the same
# line
for i in range(len(cities)):
    print(f"Daily cost of {cities[i]} is ${cities_daily_cost[i]}")
