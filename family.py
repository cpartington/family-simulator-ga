from person import Person


class Family:
    def __init__(self, husband: Person, wife: Person, family_line: int =None):
        self.husband = husband
        self.wife = wife
        self.children = []
        self.family_line = family_line

    def add_child(self, child):
        self.children += [child]

    def __str__(self):
        return 'Parents (Family Line {}):\n' \
               '{}{}' \
               'Children:\n' \
               '{}'\
            .format(self.family_line, self.husband, self.wife, ''.join([str(c) for c in self.children]))
