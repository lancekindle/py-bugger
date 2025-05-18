"""A simple script with a function call result accessed using dict key"""

def get_person():
    """Return a simple person dictionary with name and age."""
    return {"name": "Alice", "age": 30}

# Get a person and access using dict key
person = get_person()
name = person["name"]
print(f"The person's name is {name}")