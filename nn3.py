from abc import ABC, abstractmethod


# Core Engine
class GameEngine:
    def __init__(self):
        self.modules = []  # List of modules, such as input handling or game logic
        self.pieces = []   # List of game pieces (player, enemies, etc.)
        self.running = True  # Engine running flag

    def add_module(self, module):
        """Add a module to the engine."""
        if isinstance(module, Module):
            self.modules.append(module)
        else:
            raise TypeError("Only instances of Module can be added as modules.")

    def add_piece(self, piece):
        """Add a game piece to the engine."""
        if isinstance(piece, Piece):
            self.pieces.append(piece)
        else:
            raise TypeError("Only instances of Piece can be added as pieces.")
        
    def update_pieces(self):
        # Update all pieces
        for piece in self.pieces:
            piece.update()
            
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
                self.update_pieces()   
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
        self.data = []  # Optional data for game-specific logic

    def update(self):
        """Update piece state."""
        pass


# Player Piece
class Player(Piece):
    def __init__(self):
        super().__init__("Player", "The main character of the game.")

    def update(self):
        """Player-specific update logic."""
        print(f"{self.name} is standing by.")


# Input Mapping Module
class InputMap(Module):
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
class Quit(Command):
    def __init__(self, engine):
        super().__init__('quit')
        self.engine = engine

    def execute(self):
        print("Thank you for playing!")
        self.engine.running = False  # Stop the game loop


# Room Module
class RoomModule(Piece):
    def __init__(self, room_name, description):
        super().__init__(room_name, description)

    def update(self):
        print(f"You are in {self.name}. {self.description}")


# Example Usage
def main():
    # Initialize the game engine
    engine = GameEngine()

    # Add room modules to the engine
    engine.add_piece(RoomModule("Lab 1", "A dark, spooky forest with tall trees."))
    engine.add_piece(RoomModule("Lab 2", "A calm river flows here."))
    engine.add_piece(Player())

    # Create an input map and add commands
    input_map = InputMap()
    input_map.add_command(Quit(engine))  # Add the Quit command to stop the engine
    engine.add_module(input_map)

    # Run the game
    engine.run()


if __name__ == "__main__":
    main()
