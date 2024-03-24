import datetime


class Project:
    """Represent Project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise project name, start date, priority, completion percentage, and cost."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __gt__(self, other):
        """Return start dates that are after the entered date."""
        return self.start_date > other.start_date

    def __lt__(self, other):
        """Return from the lowest priority to highest."""
        return self.priority < other.priority

    def __str__(self):
        """Return data about project: name, start date, priority, completion percentage, and cost."""
        return f" {self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}" \
               f", estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"

    def is_unfinished(self, MAXIMUM_PERCENTAGE=100):
        """Returns True for projects that are incomplete."""
        if self.completion_percentage != MAXIMUM_PERCENTAGE:
            return True

    def is_updated_completion_percentage(self, entered_percentage):
        """Update completion percentage from entered percentage."""
        self.completion_percentage = entered_percentage

    def is_updated_priority(self, new_priority):
        """Update priority from user's input"""
        self.priority = new_priority
