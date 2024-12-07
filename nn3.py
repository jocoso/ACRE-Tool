# Abstract Base Class for Modules
class Module(ABC):
    @abstractmethod
    def execute(self):
        """Executes the module's functionality."""
        pass

# Abstract Base Class for Pieces (like Player)
class Piece(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.data = []

    def update(self):
        """Update the Piece (e.g., player behavior or status)."""
        pass

class Player(Piece):
    def __init__(self):
        super().__init__("player piece", "Main player character.")
        
    def update(self):
        # Implement player-specific update behavior here
        pass

# Abstract Base Class for Commands
class Command(Module):
    def __init__(self, trigger):
        super().__init__()
        self.trigger = trigger  # Command trigger word or phrase

    def validate(self, user_input):
        """Default validation logic: check if the input matches the trigger."""
        return user_input.strip().lower() == self.trigger

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

# Concrete Command Class: Quit
class Quit(Command):
    def __init__(self):
        super().__init__('quit')  # Initialize the command with its trigger word

    def execute(self):
        print("Thank you for playing!")
        exit(0)

# Concrete Module Class: RoomModule (used to display rooms)
class RoomModule(Module):
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description

    def execute(self):
        print(f"You are in {self.room_name}. {self.description}")

# Example Usage
engine = GameEngine()

# Add room modules to the game engine
engine.add_module(RoomModule("Lab 1", "A dark, spooky forest with tall trees."))
engine.add_module(RoomModule("Lab 2", "A calm river flows here."))

# Create and add InputMap with commands
input_map = InputMap()
input_map.add_command(Quit())  # Add the Quit command to InputMap
engine.add_module(input_map)  # Add InputMap to GameEngine

# Run the game engine
engine.run()
