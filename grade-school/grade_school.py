class School(object):
    def __init__(self, name):
        self.name = name
        self.grades = [set() for _ in range(8)]

    def add(self, name, grade):
        """Add a student's name to the roster for a grade."""
        self.grades[grade-1].add(name)

    def grade(self, grade):
        """Get a list of all students enrolled in a grade."""
        return self.grades[grade-1]

    def sort(self):
        """
        Get a sorted list of all students in all grades.
        Grades should sort as 1, 2, 3, etc., and students
        within a grade should be sorted alphabetically by name.
        """
        return [(idx+1, tuple(sorted(roster)))
                for idx, roster in enumerate(self.grades) if roster]
