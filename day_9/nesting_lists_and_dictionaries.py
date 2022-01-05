capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Uganda": "Kampala",
    "DRC": "Kinshasa",

}

# Nesting a list of visited cities for each country in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Uganda": ["Kampala", "Jinja", "Kasese", "Bwera", "Mbarara", "Masaka"],
    "DRC": ["Kinshasa", "Goma", "Butembo", "Beni", "Kisangani", "Lubumbashi"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities-visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany": {"cities-visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
    "Uganda": {"cities-visited": ["Kampala", "Jinja", "Kasese", "Bwera", "Mbarara", "Masaka"], "total_visits":10},
    "DRC": {"cities-visited": ["Kinshasa", "Goma", "Butembo", "Beni", "Kisangani", "Lubumbashi"], "total_visits" : 8}
}

# Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities-visited": ["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    {
        "country": "Germany",
        "cities-visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
    {
        "country": "Uganda",
        "cities-visited": ["Kampala", "Jinja", "Kasese", "Bwera", "Mbarara", "Masaka"],
        "total_visits":10
    },
    {
        "country": "DRC",
        "cities-visited": ["Kinshasa", "Goma", "Butembo", "Beni", "Kisangani", "Lubumbashi"],
        "total_visits" : 8
    }
]


