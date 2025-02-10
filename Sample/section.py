import os
import textwrap
from typing import List, Optional, Dict, Callable
from abc import ABC, abstractmethod
from pynput.keyboard import Key

class ContentNotFoundError(IndexError):
    """Custom exception raised when content is not found."""
    pass

class Section(ABC):
    """
    Represents a section of content.
    """

    END_OF_SECTION_MARKER = "--END OF SECTION--"

    def __init__(self,
                 section_title: str,
                 section_description: str):
        """
        Initializes a Section object.

        Args:
            section_title (str): The title of the section.
            section_description (str): A description of the section.
        """
        self.section_title = section_title
        self.section_description = section_description
        self.section_content: List[str] = [Section.END_OF_SECTION_MARKER]
        self.section_is_read = False
        self.section_input: Dict[Key, Callable] = {}
        
        self.add_input(Key.right, self.next_page)
        self.add_input(Key.left, self.previous_page)
        self.page_index = 0

    def add_input(self, key: Key, function: Callable):
        self.section_input[key] = function
    def add_content(self, content: str) -> int:
        """Adds content to the section before the end marker."""
        self.section_content.insert(len(self.section_content) - 1, content)
        return len(self.section_content) - 2

    def toggle_read(self) -> bool:
        """Toggles the read status of the section."""
        self.section_is_read = not self.section_is_read
        return self.section_is_read

    def has_been_read(self) -> bool:
        """Checks if the section has been read."""
        return self.section_is_read

    def retrieve_content(self, id: int) -> Optional[str]:
        """Retrieves content by its ID."""
        try:
            return self.section_content[id]
        except IndexError:
            raise ContentNotFoundError(f"Content with ID {id} not found.")

    def is_name(self, name: str) -> bool:
        """Checks if the given name matches the section's title."""
        return self.section_title.lower() == name.lower()

    def get_name(self) -> str:
        """Returns the section title."""
        return self.section_title

    def update_name(self, new_name: str) -> None:
        """Updates the title of the section."""
        if not new_name.strip():
            raise ValueError("Section title cannot be empty.")
        self.section_title = new_name

    def get_description(self) -> str:
        """Returns the description of the section."""
        return self.section_description

    def update_description(self, new_description: str) -> None:
        """Updates the description of the section."""
        self.section_description = new_description

    def next_page(self) -> None:
        """Advances to the next page of content."""
        if self.page_index < len(self.section_content) - 1:
            self.page_index += 1

    def previous_page(self) -> None:
        """Goes back to the previous page of content."""
        if self.page_index > 0:
            self.page_index -= 1

    def display(self, width: int = 80) -> None:
        """Displays the content of the section."""
        os.system('cls' if os.name == 'nt' else 'clear')
        if 0 <= self.page_index < len(self.section_content):
            content = self.section_content[self.page_index]
            wrapped_text = textwrap.fill(content, width=width)
            print(wrapped_text)
        else:
            print("Error: Page index out of bounds")

    @abstractmethod
    def update(self, key: str) -> None:
        """Update the section's state (e.g., animation, timers)."""
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the Section object."""
        return f"Section(title='{self.section_title}', description='{self.section_description}', is_read={self.section_is_read})"

