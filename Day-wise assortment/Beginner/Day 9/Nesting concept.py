# Concept of nesting dictionaries or lists in a dictionaries itself


# First
# we are going to tackle : Nesting Dictionaries within Dictionaries
# Declaring dictionaries which can be nested in other dictionaries
# Final Dictionary
travel_log = {
    "France":
        {
            "to_be_visited": ["Paris", "Dijon"],
            "visited": ["Lille"],
        },
    "India":
        {
            "to_be_visited": ["Delhi", "Bombay"],
            "visited": ["Kolkata"],
        }
}

# Second
# we are going to tackle : Nesting Dictionaries within List
# Either we can first declare the dictionary outside the list - like we did in the first part
# OR we can directly declare it inside the list or dictionary whichever we are considering
# Final list
travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Dijon"],
        "to_be_visited": ["Lille"]
    },
    {
        "country": "India",
        "cities_visited": ["Delhi", "Bombay"],
        "to_be_visited": ["Kolkata"]
    }
]