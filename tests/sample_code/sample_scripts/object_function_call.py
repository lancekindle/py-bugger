"""A script with direct function call attribute access."""

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        return f"{self.name} is {self.age} years old"


def create_person(name, age):
    """Create and return a Person object."""
    return Person(name, age)


# Direct function call attribute access
name = create_person("Bob", 25).name  # Direct attribute access on function call
print(f"The person's name is {name}")

# Also test the indirect case (currently not supported)
person = create_person("Alice", 30)
age = person.age
print(f"The person's age is {age}")
print(f"Person info: {person.get_info()}")