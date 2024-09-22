class Car:
    # Define the possible directions and how they change
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction, commands):
        self.name = name  # Name of the car
        self.x = x  # Current x-coordinate
        self.y = y  # Current y-coordinate
        self.direction = direction  # Current facing direction (N, S, E, W)
        self.commands = commands  # Commands sequence (string of L, R, F)
        self.active = True  # Flag to check if car is active or has stopped moving

    def turn_left(self):
        # Rotate the car 90 degrees to the left
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx - 1) % 4]

    def turn_right(self):
        # Rotate the car 90 degrees to the right
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self):
        # Move the car one step forward in its current direction
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def execute_command(self, command):
        # Execute a single command
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'F':
            self.move_forward()

    def get_position(self):
        # Get the current position of the car
        return (self.x, self.y)

    def __repr__(self):
        # Display car's information
        return f"{self.name} at ({self.x},{self.y}) facing {self.direction}"
