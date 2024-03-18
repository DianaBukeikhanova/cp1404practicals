"""
Guitars!
Estimate: 35 minutes
Actual: 39 minutes
"""


class Guitar:
    """Represent Guitar object."""

    def __init__(self, name="", year=0, cost=0.1):
        """Initialise guitar name, year and cost.

        name:string
        year=integer
        cost:float"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return data about guitar: name, year, cost."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self, CURRENT_YEAR=2024):
        """Return age of the guitar based on current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return vintage status for guitars."""
        if self.get_age() >= 50:
            return True
        else:
            return False
