# sample.py

from board import Board
from typing import Dict, Any, Optional

class Section:
    """
    Represents a section of content.
    """
    def __init__(self,
            section_name: str,
            section_description: str,
            section_writer: str,
            section_developer: str):
        """
        Initializes a Section object.

        Args:
            section_name (str): The name of the section.
            section_description (str): A description of the section.
            section_writer (str): The name of the writer.
            section_developer (str): The name of the developer.
        """
        self.section_name = section_name
        self.section_description = section_description
        self.section_credit: Dict[str, str] = {
            "writer": section_writer,
            "developer": section_developer
        }
        self.section_content: list[str] = ["--END OF SECTION--"]

    def add_content(self, content: str) -> int:
        """Adds content to the section before the end marker.

        Args:
            content (str): The content to add.

        Returns:
            int: The ID (index) of the added content.
        """
        _id = len(self.section_content) - 1
        self.section_content.insert(_id, content)
        return _id

    def retrieve_content(self, _id: int) -> Optional[str]:
        """Retrieves content by its ID.

        Args:
            _id (int): The ID of the content to retrieve.

        Returns:
            str: The content, or None if the ID is invalid.

        Raises:
            IndexError: If the ID is out of range.
        """
        try:
            return self.section_content[_id]
        except IndexError as e:
            print(f"Error: Index {_id} is out of bounds. {e}") #Keep print statement to not break current implementation, remove later
            return None

    def is_name(self, name: str) -> bool:
        """
        Checks if the given name matches the section's name.

        Args:
            name (str): The name to compare.

        Returns:
            bool: True if the names match, False otherwise.
        """
        return self.section_name == name
    def get_name(self) -> str:
        """
        Returns the section name.

        Returns:
            str: The section name.
        """
        return self.section_name
    def update_name(self, new_name: str) -> None:
        """
        Updates the name of the section.

        Args:
            new_name (str): The new name for the section.
        """
        self.section_name = new_name
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
    def get_credits(self) -> Dict[str, str]:
        """
        Returns the credits for the section.

        Returns:
            dict: A dictionary containing the credits (writer, developer, etc.)
        """
        return self.section_credit
    def addto_credits(self, newcredit_role: str, newcredit_name: str) -> str:
        """
        Adds a new credit to the section.

        Args:
            newcredit_role (str): The title of the credit (e.g., "editor").
            newcredit_name (str): The name of the person being credited.

        Returns:
            str: A message indicating who was credited and for what role.
        """
        self.section_credit[newcredit_role] = newcredit_name
        return f"{newcredit_name} has been credited as {newcredit_role}"
    def remove_credit(self, existingcredit_title: str) -> Optional[str]:
        """Removes a credit from the section.

        Args:
            existingcredit_title (str): The title of the credit to remove.

        Returns:
            str: The name of the person whose credit was removed, or None if the credit doesn't exist.

        Raises:
            KeyError: If the credit title does not exist.
        """
        try:
            removed_credit = self.section_credit[existingcredit_title]
            del self.section_credit[existingcredit_title]
            return removed_credit
        except KeyError as e:
            print(e)
            return None



if __name__ == '__main__':
    # Board("test_board", (2,2)).play()
    section = Section("introduction", "An introduction to the game's rules.", "Paul Bimler", "Joshua Collado")
    introduction_id = section.add_content(
        "Welcome to Frozen Offerings, a solo (DM dree) adventure\n"
        "written especially for issue 34 of Dragon+. This solo\n"
        "adventure is played just like a game book: you read\n"
        "through text entries, make decision, and are then\n"
        "directed to further text entries, and occasional combat\n"
        "encounters."
    )
    print(f"Added content with ID: {introduction_id}")
    print(f"Content: {section.retrieve_content(introduction_id)}")
    print(section.get_credits())
    section.addto_credits("editor", "Alice")
    print(section.get_credits())
    section.remove_credit("editor")
    print(section.get_credits())
    # section.add_content_to_end("This is the very end!")
    print(section.section_content)

