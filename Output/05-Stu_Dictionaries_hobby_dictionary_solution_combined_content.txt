# Dictionary full of info
my_info = {"name": "Zendaya",
           "age": 26,
           "hobbies": ["philanthropy", 
                       "playing with animals", 
                       "fashion", 
                       "social media"],
           "wake-up": {
               "Monday": 5, 
               "Friday": 5, 
               "Saturday": 10, 
               "Sunday": 9
            }
}

# Print out results stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am {my_info["age"]} years old.')
print(f'My first hobby is {my_info["hobbies"][0]}')
print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')

# Use a loop to print out the key-value pairs in the dictionary
for key, value in my_info.items():
    print(f"{key}: {value}")

# Use a loop to print out the keys of the wake-up dictionary
for day in my_info["wake-up"].keys():
    print(day)

# Use a loop to print out the values of the wake-up dictionary
for time in my_info["wake-up"].values():
    print(time)