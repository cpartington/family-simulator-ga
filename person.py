class Person:
    def __init__(self, mother=None, father=None):
        # Basic information
        self.age: int
        self.sex: int
        self.name: str
        self.mother = mother
        self.father = father

        # Personality information
        self.rebellious: int
        self.ambition: int
        self.hardworking: int
        self.life_goal: int

        # Complex information
        self.education: int
        self.income: int
        self.lifestyle: int
        self.parenting: int

        # Automated creation
        if mother is not None and father is not None:
            self.init_self()

    def init_self(self):
        pass
