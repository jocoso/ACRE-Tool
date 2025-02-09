# sample.py

from board import Board

class Section:
    """
    Represents a section of content.
    """
    def __init__(self, 
            section_name, 
            section_description,
            section_writer,
            section_developer):
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
        self.section_credit = {
            "writer": section_writer,
            "developer": section_developer
        }
    
    def is_name(self, name):
        """
        Checks if the given name matches the section's name.

        Args:
            name (str): The name to compare.

        Returns:
            bool: True if the names match, False otherwise.
        """
        return self.section_name == name
    def get_name(self):
        """
        Returns the section name.

        Returns:
            str: The section name.
        """
        return self.section_name
    def update_name(self, new_name):
        """
        Updates the name of the section.

        Args:
            new_name (str): The new name for the section.
        """
        self.section_name = new_name
    def get_description(self):
        """
        Returns the description of the section.

        Returns:
            str: The section description.
        """
        return self.section_description
    def update_description(self, new_description):
        """
        Updates the description of the section.

        Args:
            new_description (str): The new description.
        """
        self.section_description = new_description
    def get_credits(self):
        """
        Returns the credits for the section.

        Returns:
            dict: A dictionary containing the credits (writer, developer, etc.)
        """
        return self.section_credit
    def addto_credits(self, newcredit_role, newcredit_name):
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
    def remove_credit(self, existingcredit_title):
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
    print(section.is_name("introduction")) # True
