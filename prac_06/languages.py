"""
Programming Language
Estimate: 45 minutes
Actual: 33 minutes
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Display information with ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    print("\n".join(language.field for language in languages if language.is_dynamic()))


main()
