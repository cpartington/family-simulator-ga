from person import Person


class Family:
    def __init__(self, husband: Person, wife: Person):
        self.husband = husband
        self.wife = wife
        self.children = []