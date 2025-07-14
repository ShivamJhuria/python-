def describe_car(brand, model, color):
    print(f"The car is a {color} {brand} {model}.")

# Using keyword arguments
describe_car(brand="Toyota", model="Corolla", color="Red")
describe_car(color="Blue", model="Civic", brand="Honda")