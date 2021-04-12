

class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, first_name, last_name, location_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.location_id = location_id