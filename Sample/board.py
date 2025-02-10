from typing import Dict, Optional, List
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod from abc
from input_handler import InputHandler  # Assuming you have this class
from pynput.keyboard import Key  # Import Key from pynput.keyboard


class Section:
    pass


class Board:
    def __init__(self, board_title: str, board_writer: str, board_developer: str, board_sections: List[Section], board_image=None):
        self.board_title = board_title
        self.is_running = False
        self.board_input = InputHandler("board_input")
        
        self.board_input.add_key_function(Key.esc, self.quit)

        self.board_credit: Dict[str, str] = {
            "main-writer": board_writer,
            "main-developer": board_writer  # You had 'board_developer', but it's not defined
        }

        self.board_sections = board_sections
        self.current_section_index: int = 0  # Stores current section * index *
        self.current_section: Optional[Section] = None
        if self.board_sections:
            self.current_section = self.board_sections[0]  # at index 0 of board_sections
        else:
            print("Warning: Board initialized with no sections.")  # Handle empty case

    def quit(self):
        self.is_running = False

    def get_credits(self) -> Dict[str, str]:
        return self.board_credit

    def add_to_credits(self, newcredit_role: str, newcredit_name: str) -> str:
        self.board_credit[newcredit_role] = newcredit_name
        return f"{newcredit_name} has been credited as {newcredit_role}"

    def remove_credit(self, existingcredit_title: str) -> Optional[str]:
        try:
            removed_credit = self.board_credit[existingcredit_title]
            del self.board_credit[existingcredit_title]
            return removed_credit
        except KeyError as e:
            print(f"Error removing credit: {e}")  # Consider logging instead
        return None

    def on_release(self, key):
        # if self.board_input.handle_input(key):  # Assuming you want to get rid of the input_handler
        try:
            if key == Key.esc:
                self.quit()
            print(f"Key {key} released")
        except AttributeError:
            print(f"Special key {key} released")

    def play(self):
        self.is_running = True

        while self.is_running:
            print("Board is running...")
            if self.current_section:
                self.current_section.display()
            else:
                print("No sections to display.")
                self.is_running = False  # Exit if there are no sections
                break

            user_input = input(">").strip().lower()

            try:
                # Advance to the next section
                if self.current_section_index < len(self.board_sections) - 1:  # Check if incrementing is safe
                    self.current_section_index += 1
                    self.current_section = self.board_sections[self.current_section_index]
                else:
                    print("End of board reached!")
                    self.is_running = False  # Or loop back to the start
            except NotImplementedError as e:
                print(f"Section missing implementation: {e}")
                self.is_running = False

