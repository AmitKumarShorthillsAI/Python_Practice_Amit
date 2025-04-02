from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.year = year  # Public attribute
    
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method (must be implemented by subclasses)
    
    @abstractmethod
    def stop_engine(self):
        pass  # Abstract method
    
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model} ({self.year})")

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type  # Additional attribute
    
    def start_engine(self):
        print(f"{self.brand} {self.model}: Engine started with {self.fuel_type}.")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model}: Engine stopped.")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  # Additional attribute
    
    def start_engine(self):
        print(f"{self.brand} {self.model}: Electric motor started with {self.battery_capacity} kWh battery.")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model}: Electric motor stopped.")

# Execution
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2023, "Gasoline")
    ev = ElectricCar("Tesla", "Model S", 2022, 100)
    
    print("\nVehicle Information:")
    car.display_info()
    ev.display_info()
    
    print("\nStarting Engines:")
    car.start_engine()
    ev.start_engine()
    
    print("\nStopping Engines:")
    car.stop_engine()
    ev.stop_engine()
