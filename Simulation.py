class Simulation:
    def __init__(self):
        self.field = None  # The field for the simulation

    def start(self):
        # Start the simulation
        print("Welcome to Auto Driving Car Simulation!")
        self.initialize_field()
        self.main_menu()

    def initialize_field(self):
        # Initialize the field with user-specified dimensions
        while True:
            try:
                width, height = map(int, input(
                    "Please enter the width and height of the simulation field in x y format: ").split())
                if width > 0 and height > 0:
                    from Field import Field
                    self.field = Field(width, height)
                    print(f"You have created a field of {width} x {height}.\n")
                    break
                else:
                    print("Error: Width and height must be positive integers.")
            except ValueError:
                print("Error: Invalid input. Please enter two integers for width and height.")

    def main_menu(self):
        # Display main menu options
        while True:
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input().strip()
            if choice == "1":
                self.add_car()
            elif choice == "2":
                if len(self.field.cars) > 0:
                    self.run_simulation()
                    break  # Exit after running the simulation
                else:
                    print("No cars have been added to the field. Please add a car first.")
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def add_car(self):
        # Add a car to the field based on user input
        name = input("Please enter the name of the car: ").strip()
        while True:
            try:
                x, y, direction = input(
                    f"Please enter initial position of car {name} in x y Direction format: ").split()
                x, y = int(x), int(y)
                from Car import Car
                if direction not in Car.DIRECTIONS:
                    raise ValueError("Invalid direction")
                if self.field.is_within_bounds(x, y):
                    commands = input(f"Please enter the commands for car {name} (only L, R, F are allowed): ").strip()
                    if all(c in 'LRF' for c in commands):
                        car = Car(name, x, y, direction, commands)
                        self.field.add_car(car)
                        print(f"Added car {car}\n")
                        break
                    else:
                        print("Invalid commands. Please use only 'L', 'R', and 'F'.")
                else:
                    print(f"Error: Position ({x},{y}) is out of field bounds.")
            except ValueError:
                print("Invalid input. Please enter in the format: x y Direction.")

    def run_simulation(self):
        print("\nYour current list of cars are:")
        for car in self.field.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {car.commands}")

        print("\nStarting simulation...\n")

        # Initialize variables for running the simulation for all cars
        step = 0
        collision_detected = False

        # Continue while at least one car is still active
        while any(car.active for car in self.field.cars):
            for car in self.field.cars:
                if car.active and step < len(car.commands):
                    # Execute the next command for the car
                    car.execute_command(car.commands[step])

                    # Check if the car is still within the field
                    if not self.field.is_within_bounds(car.x, car.y):
                        print(f"Car {car.name} moved out of bounds at ({car.x}, {car.y}) and has stopped moving.")
                        car.active = False
                        continue

                    # Check for collision after each command execution
                    collision = self.field.detect_collision()
                    if collision:
                        car1, car2 = collision
                        car1.active = False
                        car2.active = False
                        print(
                            f"Collision detected between car {car1.name} and car {car2.name} at position ({car1.x}, {car1.y}) at step {step + 1}.")
                        collision_detected = True
                        break

                # Deactivate the car if it has finished executing all commands
                if step >= len(car.commands):
                    car.active = False

            if collision_detected:
                break

            step += 1  # Move to the next step

        print("Simulation completed.\nFinal positions of all cars:")
        for car in self.field.cars:
            status = "Stopped" if not car.active else "Active"
            print(f"- {car.name}, Position: ({car.x},{car.y}), Facing: {car.direction}, Status: {status}")

        self.post_simulation_menu()

    def post_simulation_menu(self):
        # Post-simulation options
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            choice = input().strip()
            if choice == "1":
                self.start()
                break
            elif choice == "2":
                print("Thank you for running the simulation. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
