from abc import ABC, abstractmethod

# Core Engine
class GameEngine:
    def __init__(self, player):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def run(self):
        while True:
            for module in self.modules:
                module.execute()

class Module(ABC):
    @abstractmethod
    def execute(self):
        """Executes module"""
        pass

class Piece(ABC):
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.data = []
        
    def update(self):
        """Update Piece"""
        pass
    
    
class Player(Piece):
    def __init__(self):
        super().__init__(self, "player piece", "main player.")
    def update(self):
        pass
                
class InputMap(Module):
    def __init__(self):
        self.commands = []
        self.user_input = ""
        
    def add_command(self, command):
        if isinstance(command, Command):
            self.commands.append(command)
            
    def execute(self):
        self.user_input = input(">: ")
        for command in self.commands:
            if command.validate(self.user_input):
                command.execute()
            else:
                print("This command cannot be understood.")
                
# Abstract Base Class for Commands
class Command(Module):
    @abstractmethod
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
# A Module

class Quit(Command):
    def __init__(self):
        super().__init__('quit')  # Correct usage of super()

    def execute(self):
        print("Thank you for playing!")
        exit(0)

class RoomModule(Module):
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description

    def execute(self):
        print(f"You are in {self.room_name}. {self.description}")

# Example Usage

engine = GameEngine()
engine.add_module(RoomModule("Lab 1", "A dark, spooky forest with tall trees."))
engine.add_module(RoomModule("Lab 2", "A calm river flows here."))

input_map = InputMap()
input_map.add_command(Quit())
engine.add_module(input_map)

engine.run()
