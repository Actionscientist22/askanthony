"""Refactoring the travel loops code."""

def travel_cities(cities, cities_daily_cost):
    """
    Update the city list and its corresponding daily cost list.

    This function prompts the user to add cities to the city list and their
    respective daily costs. It then modifies the daily cost by adding 10 to
    each item. Finally, it displays the city and its updated daily cost.

    Args:
        cities (list): A list of cities.
        cities_daily_cost (list): A list of daily costs corresponding to the cities.
    Returns:
        The list of cities with the daily cost for each city.
    """

    print("Here are the cities in the current list:")
    for city in cities:
        print(city)
    print("Please add 3 cities to the list of cities:")
    # Create a for loop to ask the user to enter a city that will be added to the list.
    for _ in range(3):
        city = input("What city should be added to the list? ").title()
        cities.append(city)

    # Use a while loop to append to the cities_daily_cost list as long as that list
    # is shorter than the cities list
    while len(cities_daily_cost) < len(cities):
        # Use the length of cities_daily_cost for the index of cities to print its
        # value when asking the cost to append to the cities_daily_cost list
        index = len(cities_daily_cost)
        cost = int(input(f"What is the daily cost for {cities[index]}? "))
        cities_daily_cost.append(cost)

    # Loop through the cities_daily_cost list and add 10 to each item
    for i, cost in enumerate(cities_daily_cost):
        cities_daily_cost[i] += 10

    # Use a for loop to loop through both of the lists at the same time, since
    # they're the same length, and print out the city and daily cost on the same
    # line
    for i, city in enumerate(cities):
        print(f"Daily cost of {city} is ${cities_daily_cost[i]}")

if __name__ == "__main__":

    # Declare lists
    cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
    cities_daily_cost = [150, 70, 60, 80, 110, 125]

    # Call the function
    travel_cities(cities, cities_daily_cost)
