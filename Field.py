class Field:
    def __init__(self, width, height):
        self.width = width  # Width of the field
        self.height = height  # Height of the field
        self.cars = []  # List of cars in the field

    def add_car(self, car):
        # Add a new car to the field
        self.cars.append(car)

    def is_within_bounds(self, x, y):
        # Check if a given position is within the field's boundaries
        return 0 <= x < self.width and 0 <= y < self.height

    def detect_collision(self):
        # Check if any cars have collided on the field
        positions = {}
        for car in self.cars:
            if car.active:
                pos = car.get_position()
                if pos in positions:
                    return positions[pos], car  # Return the two colliding cars
                positions[pos] = car
        return None  # No collision detected
