from abc import ABC, abstractmethod

# Core Engine
class GameEngine:
    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def run(self):
        while True:
            for module in self.modules:
                module.execute()
            
class InputMap:
    def __init__(self):
        self.commands = []
        self.user_input = ""
        
    def add_command(self, command):
        if isinstance(command, Command):
            self.commands.append(command)
            
    def listen(self):
        self.user_input = input(">: ")
        for command in self.commands:
            if command.validate(self.user_input):
                command.exec()
            else:
                print("This command cannot be understood.")
        

# Abstract Base Class for Commands
class Command(ABC):
    @abstractmethod
    def __init__(self, trigger):
        self.trigger = trigger  # Command trigger word or phrase

    def validate(self, user_input):
        """Default validation logic: check if the input matches the trigger."""
        return user_input.strip().lower() == self.trigger

    @abstractmethod
    def exec(self):
        """Execute the command."""
        pass
# A Module

class Quit(Command):
    def __init__(self):
        super().__init__('quit')  # Correct usage of super()

    def exec(self):
        print("Thank you for playing!")
        exit(0)

class RoomModule:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description

    def execute(self):
        print(f"You are in {self.room_name}. {self.description}")

# Example Usage
input_map = InputMap()
input_map.add_command(Quit())
engine = GameEngine(input_map)
engine.add_module(RoomModule("Lab 1", "A dark, spooky forest with tall trees."))
engine.add_module(RoomModule("Lab 2", "A calm river flows here."))
engine.run()
