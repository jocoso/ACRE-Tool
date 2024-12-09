"""
Author: Joshua Collado Soler
Date: December 9, 2024
Project: Player Name Validation Suite
Description:
    This script is designed to validate and format player names according to
    game-specific rules. It includes comprehensive testing for valid and invalid
    names, logging of results, and name normalization methods.

Acknowledgments:
    Special thanks to the open-source community for inspiration and support.

License:
    All rights reserved by Joshua Collado Soler. Sharing or reusing this code requires attribution.
"""


import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AskPlayerNameTestSuite:

    def __init__(self):
        self.attributes = {'name': "noor"}
        self.test_names = [
            # Valid Names
            "Noor", "Jean-Paul", "O'Connor", "Ava",
            "LoremIpsumDolorSitAmetConsecteturAdipiscingElit",
            # Invalid Names - Length
            "A", "Lo", "LoremIpsumDolorSitAmetConsecteturAdipiscingElit12345",
            # Invalid Names - Special Characters
            "John@", "M@ry#", "Asterisk*Name",
            # Invalid Names - Spaces
            " Noor ", "Noor El Amin", "   ",
            # Invalid Names - Hyphen/Apostrophe Misuse
            "-Noor", "Noor-", "'Noor", "Noor'",
            # Edge Cases
            "-----", "''''''", "12345", "Noor123",
            "Lo@rem Ipsum's Name--", "", "Nooré", "نور", "山田太郎", "Анна", "Noör"
        ]

    def has_passed_test(self, test_purpose, test_succeeded):
        status = "PASSED" if test_succeeded else "FAILED"
        logger.info(f'\t{test_purpose}: {status}')

    def normalize_input(self):
        """Validate the input name."""
        current_name = self.attributes['name']
        logger.info(f'Validating name: "{current_name}"')

        # Check individual conditions
        validations = {
            "Name length is between 3 and 50 characters": self._is_valid_length(current_name),
        "Name has no invalid special characters": self._has_no_special_characters(current_name),
        }
        
        for purpose, result in validations.items():
            self.has_passed_test(purpose, result)
        
        return all(validations.values())

    def _is_valid_length(self, name):
        return 3 <= len(name) <= 50

    def _has_no_special_characters(self, name):
        return re.search("[^a-zA-Z0-9\s'-]", name) is None

    def trim_spaces(self):
        current_name = self.attributes['name']
        stripped_name = current_name.strip()
        formatted_name = stripped_name.replace(' ', '-')
        logger.info(f'Trimmed spaces: "{current_name}" -> "{formatted_name}"')
        self.attributes['name'] = formatted_name

    def to_lower(self):
        current_name = self.attributes['name']
        lowercased_name = current_name.lower()
        logger.info(f'Lowercased name: "{current_name}" -> "{lowercased_name}"')
        self.attributes['name'] = lowercased_name

    def test(self):
        for idx, name in enumerate(self.test_names, start=1):
            logger.info(f'\nTest Case {idx}: Testing name: "{name}"')
            self.attributes['name'] = name.strip()

            validations_passed = self.normalize_input()
            self.trim_spaces()
            self.to_lower()

            final_name = self.attributes['name']
            logger.info(f'Final processed name: "{final_name}"\n')

            assert validations_passed, f"Validation failed for name: {name}"
            assert final_name, "Final name is empty!"


if __name__ == '__main__':
    AskPlayerNameTestSuite().test()
