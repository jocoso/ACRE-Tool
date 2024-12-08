class AskPlayerNameTestSuite:

    def __init__(self):
        """The name of the character as given by the player"""
        self.attributes = {'name': "noor"}
        self.test_names = [
            # Valid Names
            "Noor",  # Valid default name
            "Jean-Paul",  # Valid name with hyphen
            "O'Connor",  # Valid name with apostrophe
            "Ava",  # Short valid name
            "LoremIpsumDolorSitAmetConsecteturAdipiscingElit",  # 50 characters, valid

            # Invalid Names - Length
            "A",  # Too short (1 character)
            "Lo",  # Too short (2 characters)
            "LoremIpsumDolorSitAmetConsecteturAdipiscingElit12345",  # Too long (51 characters)

            # Invalid Names - Special Characters
            "John@",  # Contains invalid special character
            "M@ry#",  # Multiple invalid special characters
            "Asterisk*Name",  # Contains invalid special character

            # Invalid Names - Spaces
            " Noor ",  # Leading and trailing spaces
            "Noor El Amin",  # Spaces in the middle
            "   ",  # Only spaces

            # Invalid Names - Hyphen/Apostrophe Misuse
            "-Noor",  # Starts with a hyphen
            "Noor-",  # Ends with a hyphen
            "'Noor",  # Starts with an apostrophe
            "Noor'",  # Ends with an apostrophe

            # Edge Cases
            "-----",  # Only hyphens
            "''''''",  # Only apostrophes
            "12345",  # Contains only numbers
            "Noor123",  # Mix of valid name and numbers
            "Lo@rem Ipsum's Name--",  # Mix of multiple invalid elements
            "",  # Empty string
            "Nooré",  # Contains accented character
            "نور",  # Arabic script
            "山田太郎",  # Japanese script
            "Анна",  # Cyrillic script
            "Noör"  # Contains diacritic character
        ]

    def has_passed_test(self, test_purpose, test_succeeded):
        print(f'\t{test_purpose}: {"PASSED" if test_succeeded else "FAILED"}.')

    def _normalize_input(self):
        """Assures that user inputs are properly formatted."""
        print(f'Checking length constraints for: "{self.attributes["name"]}"...')

        current_name = self.attributes['name']

        lt_50 = len(current_name) <= 50 
        boe_3 = len(current_name) >= 3

        valid_name = lt_50 and boe_3

        self.has_passed_test("Name length is between 3 and 50 characters", valid_name)

    def trim_spaces(self):
        """Assures that white spaces are dealt with consistently."""
        print(f'trimming {self.attributes["name"]} spaces...')

    def to_lower(self):
        """Returns a lowercase version of the name."""
        print(f'lowercasing {self.attributes["name"]}...')

    def update(self):
        for idx, name in enumerate(self.test_names, start=1):
            self.attributes['name'] = name  # Update the name being tested
            print(f'Test Case {idx}: Testing name: {name}')
            self._normalize_input()
            self.trim_spaces()
            self.to_lower()


if __name__ == '__main__':
    AskPlayerNameTestSuite().update()
