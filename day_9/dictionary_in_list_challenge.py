"""The challenge is to write a program that adds to a travel_log, which is a list that contains 4 Dictionaries.
    Basically, we're gonna write a function to add the entry for a country to the travel_log."""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 3,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]

    },
    {
        "country": "Uganda",
        "visits": 6,
        "cities_visited": ["Kampala", "Jinja", "Kasese", "Bwera", "Mbarara", "Masaka"]

    },
    {
        "country": "DRC",
        "visits": 8,
        "cities_visited": ["Kinshasa", "Goma", "Butembo", "Beni", "Kisangani", "Lubumbashi"]
    }
]


# Function to add a country to the travel_log list
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {"country": country_visited, "visits": times_visited, "cities_visited": cities_visited}
    travel_log.append(new_country)


# Call the function to populate the country to the travel_log list
add_new_country("Rwanda", 2, ["Kigali", "Gisenyi"])

# Print the travel_log list
print(travel_log)
