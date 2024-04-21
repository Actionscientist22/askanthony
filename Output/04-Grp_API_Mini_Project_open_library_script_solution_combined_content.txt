# Import dependencies
import requests
import json

# Set up author query url
author_query_url = "https://openlibrary.org/search/authors.json?q="

print("Welcome to the interactive library.")

while True:
    print("Would you like to look up an author? ")
    use_library = input("Type 'n' to quit or anything else to continue. ")

    if use_library.lower() == 'n':
        break

    author = input("Which author would you like to search for? ")

    # Execute `GET` request with url
    response_data = requests.get(author_query_url + author)

    # Format data as JSON
    data = response_data.json()

    # Extract "key" from first result
    try:
        author_key = data["docs"][0]["key"]
        print(author_key)
        author_found = True
    except:
        print("Couldn't find author. Try again.")
        author_found = False


    if author_found:
        # Use author key to fetch author's works
        author_works_url = f"https://openlibrary.org/authors/{author_key}/works.json"

        # Execute `GET` request with url
        response_data = requests.get(author_works_url)

        # Format data as JSON
        author_works_data = response_data.json()

        while True:
            # Print menu of results: 
            print("Select the number for the book you would like to view.")
            for i in range(len(author_works_data["entries"])):
                print(f'{i}: {author_works_data["entries"][i]["title"]}')

            work_selection = input("What is your selection? ")

            try:
                work_selection = int(work_selection)
                work_title = author_works_data["entries"][work_selection]["title"]
                work_url = "https://openlibrary.org" \
                           + author_works_data["entries"][work_selection]["key"]
                
                # Execute `GET` request with url
                work_response_data = requests.get(work_url + ".json")
                work_data = work_response_data.json()

                print("JSON Data:")

                # Dump JSON about work
                print(json.dumps(work_data, indent=4))

                print(f"Visit {work_url} for information about {work_title}")
            except:
                print("Your chosen selection could not be looked up.")

            print("Would you like to look up another work from this author?")
            another_work = input("Type 'y' for yes, anything else to return to "
                                + "author search. ")
            
            if another_work.lower() != "y":
                break
