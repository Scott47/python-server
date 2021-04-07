LOCATIONS = [
   {
    "id": 1,
    "name": "Scooby Villa North",
    "address": "321 Zoiks Lane, Nashville, TN"
   },
   {
    "id": 2, 
    "name": "McGruff Kenneltentiary",
    "address": "911 Crime Dog Way"
   }
]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location