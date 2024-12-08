from abc import ABC, abstractmethod


# Core Engine
class GameEngine:
    def __init__(self):
        self.modules = []  # List of modules, such as input handling or game logic
        self.running = True  # Engine running flag

    def add_module(self, module):
        """Add a module to the engine."""
        if isinstance(module, Module):
            self.modules.append(module)
        else:
            raise TypeError("Only instances of Module can be added as modules.")
            
    def update_modules(self):
        # Execute all modules
        for module in self.modules:
            module.execute()
    
    def handle_error(self, message):
        print(f"An error occurred: {message}")
        self.running = False

    def run(self):
        """Main game loop."""
        print("Game starting. Type 'quit' to exit.")
        while self.running:
            try: 
                self.update_modules()
            except Exception as e:
                self.handle_error(e)


# Abstract Module Base Class
class Module(ABC):
    @abstractmethod
    def execute(self):
        """Executes module logic."""
        pass


# Abstract Piece Base Class
class Piece(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def update(self):
        """Update piece state."""
        pass


# Player Piece
class PlayerPiece(Piece):
    def __init__(self):
        super().__init__("Player", "The main character of the game.")

    def update(self):
        """Player-specific update logic."""
        print(f"{self.name} is ready for action.")


# Input Mapping Module
class InputMapModule(Module):
    def __init__(self):
        self.commands = {}  # Dictionary to store commands by trigger

    def add_command(self, command):
        """Add a command to the input map."""
        if isinstance(command, Command):
            self.commands[command.trigger] = command
        else:
            raise TypeError("Only instances of Command can be added as commands.")

    def execute(self):
        """Handle user input and execute commands."""
        user_input = input(">: ").strip().lower()
        command = self.commands.get(user_input)
        if command:
            command.execute()
        else:
            print("This command cannot be understood.")


# Abstract Command Base Class
class Command(ABC):
    def __init__(self, trigger):
        self.trigger = trigger  # Command trigger word or phrase

    def validate(self, user_input):
        """Default validation logic: check if the input matches the trigger."""
        return user_input.strip().lower() == self.trigger

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass


# Quit Command
class QuitCommand(Command):
    def __init__(self, engine):
        super().__init__('quit')
        self.engine = engine

    def execute(self):
        print("Thank you for playing!")
        self.engine.running = False  # Stop the game loop


# Room Piece
class RoomPiece(Piece):
    def __init__(self, room_name, description):
        super().__init__(room_name, description)

    def update(self):
        print(f"You are in {self.name}. {self.description}")


# Map Grid Module
class MapGridModule(Module):
    class Vector:
        def __init__(self, x=None, y=None):
            self.x = x
            self.y = y

        def is_valid(self):
            return self.x is not None and self.y is not None

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.map_grid = [[None for _ in range(size_x)] for _ in range(size_y)]

    def add_room(self, room_piece, location=None):
        if location and location.is_valid():
            if self.map_grid[location.y][location.x] is None:
                self.map_grid[location.y][location.x] = room_piece
                print(f"Room '{room_piece.name}' added at ({location.x}, {location.y}).")
            else:
                print(f"Location ({location.x}, {location.y}) is already occupied.")
        else:
            print("Invalid location provided.")

    def execute(self):
        """Display the map grid."""
        print("Map Grid:")
        for row in self.map_grid:
            print(" | ".join(room.name if room else "Empty" for room in row))


# Example Usage
def main():
    # Initialize the game engine
    engine = GameEngine()

    # Add pieces to the engine
    room1 = RoomPiece("Lab 1", "A dark, spooky forest with tall trees.")
    room2 = RoomPiece("Lab 2", "A calm river flows here.")
    # Add MapGridModule and populate it
    map_module = MapGridModule(2, 2)  # A 2x2 grid
    map_module.add_room(room1, MapGridModule.Vector(0, 0))
    map_module.add_room(room2, MapGridModule.Vector(1, 0))

    engine.add_module(map_module)

    # Create an input map and add commands
    input_map_module = InputMapModule()
    input_map_module.add_command(QuitCommand(engine))  # Add the Quit command
    engine.add_module(input_map_module)

    # Run the game
    engine.run()


if __name__ == "__main__":
    main()
