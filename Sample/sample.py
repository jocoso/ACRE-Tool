# sample.py
from board import Board
from section import Section
from pynput import keyboard

class Introduction(Section):
	def __init__(self):
		super().__init__("introduction", "An introduction to the game's rules.")
		self.completed = False
		self.section_input.add_key_function(keyboard.Key.right, self.next_page)
		self.section_input.add_key_function(keyboard.Key.left, self.previous_page)
	
	def update(self, key: any):
		self.section_input.handle_input(key)
		

if __name__ == '__main__':
    # Board("test_board", (2,2)).play()
    introduction_section = Introduction()
    introduction_section.add_content(
        "Welcome to Frozen Offerings, a solo (DM dree) adventure\n"
        "written especially for issue 34 of Dragon+. This solo\n"
        "adventure is played just like a game book: you read\n"
        "through text entries, make decision, and are then\n"
        "directed to further text entries, and occasional combat\n"
        "encounters."
    )
    introduction_section.add_content(
    	"Frozen Offerings is set in Icewind Dale, and is\n"
    	"designed for a character of 7th to 10th level and a\n"
    	"premade sidekick. This sidekick, THalgar, is introduced\n"
    	"during the backstory, and his stat blcok is located at the\n"
    	"end of the adventure text. During combat, you control\n"
    	"your character, Thalgar, and any monsters you encounter,\n"
    	"making the rolls for all of them."
    )
    
    board = Board(
    		board_title = "Frozen Offerings",
    		board_writer = "Paul Bimler",
    		board_sections = [introduction_section],
    		board_developer = "Joshua Collado")
    
    board.play()
    
    
