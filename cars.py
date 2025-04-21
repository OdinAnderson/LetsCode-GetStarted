# this file contains the class Car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is now running.")

# Create cars on the lot
car_lot = [
    Car("Toyota", "Camry", 2024),
    Car("Honda", "Civic", 2023),
    Car("Ford", "Mustang", 2024),
    Car("Tesla", "Model 3", 2024),
    Car("BMW", "X5", 2023)
]

# Display information for all cars
print("\nCars available on the lot:")
print("-" * 25)
for car in car_lot:
    car.display_info()
    print("-" * 25)

# Import matplotlib
import matplotlib.pyplot as plt

# Create lists for x and y coordinates
makes = [car.make for car in car_lot]
years = [car.year for car in car_lot]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(makes, years, color='blue', alpha=0.6, s=100)

# Customize the plot
plt.title('Car Makes vs Year')
plt.xlabel('Make')
plt.ylabel('Year')
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()