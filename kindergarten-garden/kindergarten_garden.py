class Garden(object):

    PLANTS = {
        plant[0]: plant
        for plant in 'Clover Grass Radishes Violets'.split()
    }

    def __init__(self, diagram,
                 students="Alice Bob Charlie David Eve Fred Ginny"
                          " Harriet Ileana Joseph Kincaid Larry".split()):
        self.row1, self.row2 = diagram.split()
        self.students = sorted(students)

    def plants(self, name):
        idx = self.students.index(name)
        plants = self.row1[2*idx:2*idx+2] + self.row2[2*idx:2*idx+2]
        return [self.PLANTS[plant] for plant in plants]
