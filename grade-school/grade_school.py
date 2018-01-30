class School(object):
    def __init__(self, name):
        self.name = name
        self.grades = [list() for _ in range(9)]

    def add(self, name, grade):
        """Add a student's name to the roster for a grade."""
        self.grades[grade-1].append(name)

    def grade(self, grade):
        """Get a list of all students enrolled in a grade."""
        res_grade = self.grades[grade-1]
        return tuple(res_grade) if res_grade else set()

    def sort(self):
        """
        Get a sorted list of all students in all grades.
        Grades should sort as 1, 2, 3, etc., and students
        within a grade should be sorted alphabetically by name.
        """
        return [(idx+1, tuple(sorted(roster)))
                for idx, roster in enumerate(self.grades) if roster]
