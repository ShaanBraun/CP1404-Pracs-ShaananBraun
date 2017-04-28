
class ProgrammingLanguage:

    def __init__(self, name, type, reflection, year):

        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.type, self.reflection, self.year)

    def is_dynamic(self):
        return self.type == "Dynamic"
