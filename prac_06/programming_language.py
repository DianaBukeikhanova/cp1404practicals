"""Programming Language exercise"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise field, typing, reflection, and year of entered language.

        year:integer"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True or False base on entered language typing category."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Return string with field, typing, reflection and year, based on languages file."""
        return f"{self.field}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
