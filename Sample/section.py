import os
import textwrap
from typing import List, Optional, Any
from abc import ABC, abstractmethod
from input_handler import InputHandler
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
            section_name (str): The name of the section.
            section_description (str): A description of the section.
        """
        self.section_title = section_title
        self.section_description = section_description
        self.section_content: List[str] = [Section.END_OF_SECTION_MARKER]
        self.section_is_read = False
        self.section_input = InputHandler("section_input")
        self.page_index = 0

    def add_content(self, content: str) -> int:
        """Adds content to the section before the end marker.

        Args:
            content (str): The content to add.

        Returns:
            int: The ID (index) of the added content.
        """
        self.section_content.insert(len(self.section_content) - 1, content)
        return len(self.section_content) - 2  # return index of inserted content

    def toggle_read(self) -> bool:
        """Toggles the read status of the section."""
        self.section_is_read = not self.section_is_read
        return self.section_is_read

    def has_been_read(self) -> bool:
        """Checks if the section has been read."""
        return self.section_is_read

    def retrieve_content(self, id: int) -> Optional[str]:
        """Retrieves content by its ID.

        Args:
            id (int): The ID of the content to retrieve.

        Returns:
            str: The content, or None if the ID is invalid.

        Raises:
            ContentNotFoundError: If the ID is out of range.
        """
        try:
            return self.section_content[id]
        except IndexError:
            print(f"Error: Index {id} is out of bounds.")  # Consider logging instead of printing
            return None
            # Or, you can raise the exception again:
            # raise #Re-raise the IndexError

    def is_name(self, name: str) -> bool:
        """
        Checks if the given name matches the section's name.

        Args:
            name (str): The name to compare.

        Returns:
            bool: True if the names match, False otherwise.
        """
        return self.section_title == name

    def get_name(self) -> str:
        """
        Returns the section name.

        Returns:
            str: The section name.
        """
        return self.section_title

    def update_name(self, new_name: str) -> None:
        """
        Updates the name of the section.

        Args:
            new_name (str): The new name for the section.
        """
        if not new_name:
            raise ValueError("Section name cannot be empty.")
        self.section_title = new_name

    def get_description(self) -> str:
        """
        Returns the description of the section.

        Returns:
            str: The section description.
        """
        return self.section_description

    def update_description(self, new_description: str) -> None:
        """
        Updates the description of the section.

        Args:
            new_description (str): The new description.
        """
        self.section_description = new_description

    def next_page(self) -> None:
        """Advances to the next page of content."""
        if self.page_index < len(self.section_content) - 1:
            self.page_index += 1

    def previous_page(self) -> None:
        """Goes back to the previous page of content."""
        print("Called")
        if self.page_index > 0:
            self.page_index -= 1

    def display(self, width: int = 80) -> None:
        """Displays the content of the section."""
        # TODO: Add a module to go back and forth with a mouse for reading sections.
        os.system('cls' if os.name == 'nt' else 'clear')  # cleans screen in terminal
        if 0 <= self.page_index < len(self.section_content):
            content = self.section_content[self.page_index]
            wrapped_text = textwrap.fill(content, width=width)
            print(wrapped_text)
        else:
            print("Error: Page index out of bounds")

    @abstractmethod
    def update(self, key=str):
        """Update the section's state (e.g., animation, timers)."""
        pass


    def __repr__(self) -> str:
        """Returns a string representation of the Section object."""
        return f"Section(name='{self.section_name}', description='{self.section_description}', is_read={self.section_is_read})"


