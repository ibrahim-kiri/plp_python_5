class Vehicle:
    # Base class for all vehicles with a common move method.
    def __init__(self, name, speed):
        # Initialize a Vehicle with a name and speed.
        self.name = name
        self.speed = speed

    def move(self):
        """
        Generic move method to be overridden by child classes.
        Serves as a base for polymorphic behavior.
        """
        raise NotImplementedError("Subclasses must implement move method")
    
class Car(Vehicle):
    # Represents a car with it's specific movement method.
    def move(self):
        """
        Car-specific movement method.
        Prints driving description with car's details
        """
        return f"{self.name} is driving on the road at {self.speed} km/hr"
    
class Plane(Vehicle):
    # Represents a plane with it's specific movement method
    def __init__(self, name, speed, altitude):
        # Initialize a plane with additional altitude attribute
        super().__init__(name, speed)
        self.altitude = altitude

    def move(self):
        # Plane specific movement method
        return f"{self.name} is flying at {self.speed} km/hr, altitude {self.altitude} meters"
    

class Boat(Vehicle):
    # Represents a boat with it's specific movement method
    def move(self):
        # Boat-specific movement method
        return f"{self.name} is sailing across the water at {self.speed} knots"
    
def demonstrate_polymorphism(vehicles):
    """
    Demonstrate polymorphism by calling move() on different vehicle types.
    """
    return [vehicle.move() for vehicle in vehicles]


def main():
    # Create instances of different vehicles
    tesla = Car("Tesla Model S", 250)
    boeing = Plane("Boeing 747", 907, 11000)
    yatch = Boat("Luxury Yatch", 20)

    # Create a list of Vehicles to demonstrate polymorphism
    transportation_fleet = [tesla, boeing, yatch]

    # demonstrate polympophic behavior
    movement_descriptions = demonstrate_polymorphism(transportation_fleet)

    # Print movement descriptions
    print("Polymorphism in Action:")
    for description in movement_descriptions:
        print(description)


if __name__ == "__main__":
    main()
    