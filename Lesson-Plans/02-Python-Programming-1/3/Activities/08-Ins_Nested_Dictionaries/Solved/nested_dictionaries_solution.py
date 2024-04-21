# Declare films dictionary
films = {
    "Everything Everywhere All At Once": {
        "director": ["Daniel Kwan", "Daniel Scheinert"],
        "cast": [
            "Michelle Yeoh", 
            "Ke Huy Quan", 
            "Jamie Lee Curtis", 
            "Stephanie Hsu", 
            "James Hong",
            "Jenny Slate",
            "Harry Shum Jr.",
            "Tallie Medel"
        ],
        "distributor": "A24",
        "box_office_in_millions": {
            "us": 72.1,
            "uk": 6.2,
            "canada": 5.1,
            "australia": 4.5
        },
        "release_date": {
            "us": "April 8, 2022",
            "uk": "May 13, 2022",
            "canada": "March 25, 2022",
            "australia": "April 14, 2022"
        }
    },
    "Hidden Figures": {
        "director": "Theodore Melfi",
        "writer": ["Allison Schroeder", "Theodore Melfi"],
        "cast": [
            "Taraji P. Henson", 
            "Octavia Spencer", 
            "Janelle Monáe",
            "Kevin Costner",
            "Kirsten Dunst", 
            "Jim Parsons",
            "Mahershala Ali",
            "Aldis Hodge",
            "Glen Powell"
        ],
        "distributor": "Twentieth Century Fox",
        "box_office_in_millions": {
            "us": 169.6,
            "japan": 14.1,
            "uk": 7.9,
            "australia": 13.6,
            "france": 5.6
        },
        "release_date": {
            "us": "December 25, 2016",
            "japan": "September 29, 2017",
            "uk": "February 17, 2017",
            "australia": "February 16, 2017",
            "france": "March 7, 2017"
        }
    },
    "Elemental": {
        "director": "Peter Sohn",
        "writer": ["John Hoberg", "Kat Likkel", "Brenda Hsueh"],
        "cast": [
            "Leah Lewis", 
            "Mamoudou Athie", 
            "Ronnie Del Carmen",
            "Shila Ommi",
            "Catherine O'Hara", 
            "Wendi McLendon-Covey",
            "Joe Pera"
        ],
        "distributor": "Walt Disney Studios Motion Pictures",
        "box_office_in_millions": {
            "us": 109.6,
            "south_korea": 25.9,
            "mexico": 13.5,
            "australia": 8.0,
            "france": 9.2
        },
        "release_date": {
            "us": "June 16, 2023",
            "south_korea": "June 14, 2023",
            "mexico": "June 23, 2023",
            "australia": "June 15, 2023",
            "france": "June 21, 2023"
        }
    }
}

menu_dashes = "-" * 60

# Launch the program and present a greeting to the customer
print("Welcome to the film repository.")

# Users may want to view information about different films, so let's create
# a continuous loop
while True:
    # Ask the user which film they want to view
    print("Which film would you like to view information about? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from film titles (all the first level 
    # dictionary items in films).
    for key in films.keys():
        print(f"{i}: {key}")
        # Store the film title associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the user's input
    film_selection = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if film_selection == 'q':
        break
    # Check if the user's input is a number
    elif film_selection.isdigit():
        # Check if the user's input is a valid option
        if int(film_selection) in menu_items.keys():
            # Save the film name to a variable
            film_selection_name = menu_items[int(film_selection)]
            # Print out the film they selected
            print(f"You selected {film_selection_name}")

            # Display the heading for the data
            print(menu_dashes)
            print(f"Information about {film_selection_name}")
            print(menu_dashes)
            print("Dictionary Reference                   | Information")
            print("---------------------------------------|--------------------")

            # Print out the data from the selected film
            for key, value in films[film_selection_name].items():
                # Check if the value is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the film data
                        num_item_spaces = 38 - len(key + key2) - 4
                        item_spaces = " " * num_item_spaces
                        print(f"{key}['{key2}']{item_spaces} | "
                              + f"{value2}")
                # Check if the value is a list to handle differently
                elif type(value) is list:
                    # Iterate through the list items
                    for i in range(len(value)):
                        # Print the film data
                        num_item_spaces = 38 - len(key) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{key}[{i}]{item_spaces} | "
                              + f"{value[i]}")
                else:
                    # Print the film data
                    num_item_spaces = 38 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{key}{item_spaces} | {value}")
            
            print(menu_dashes)
            input("Press enter to return to the main menu.")

        else:
            # Tell the customer they didn't select a valid option
            print(f"{film_selection} was not an option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
