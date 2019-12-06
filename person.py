class Person:
    def __init__(self):
        # Basic information
        self.age: int = -1
        self.sex: int = -1
        self.name: str = ''

        # First order information
        self.rebellious: int = -1
        self.ambition: int = -1
        self.hardworking: int = -1
        self.life_goal: int = -1
        self.lifestyle: int = -1

        # Second order information
        self.education: int = -1
        self.income: int = -1
        self.parenting_desire: int = -1
        self.parenting: int = -1
        self.longevity: int = -1

    def init_self(self, util, mother, father):
        self.age = util.random_adult_age()
        self.sex = util.random_sex()
        self.name = util.random_name(self.sex)

        self.rebellious = util.random_attribute()
        self.ambition = util.child_attribute(mother.ambition, father.ambition)
        self.hardworking = util.child_attribute(mother.hardworking, father.hardworking, self.rebellious)
        self.life_goal = util.child_life_goal(mother.life_goal, father.life_goal, self.rebellious)
        self.lifestyle = util.child_attribute(mother.lifestyle, father.lifestyle, self.rebellious)

        self.education = util.child_education(mother, father, self)
        self.income = util.child_income(self)
        self.parenting_desire = util.child_parenting_desire(mother, father, self)
        self.parenting = util.child_parenting(mother, father, self)
        self.longevity = util.child_longevity(self)

    def get_quality(self):
        q = self.ambition + self.hardworking + self.education + self.lifestyle + self.parenting
        return q

    def get_happiness(self):
        pass

    def __str__(self):
        return '{}: Age: {} Sex: {} Longevity: {}y\n' \
               '   Rebellion: {} Ambition: {} Hardworking: {}\n' \
               '   Life goal: {} Lifestyle: {} Education: {}\n' \
               '   Income: {} Parenting Desire: {} Quality: {}\n'\
            .format(self.name, self.age, self.sex, self.longevity, self.rebellious, self.ambition, self.hardworking,
                    self.life_goal, self.lifestyle, self.education, self.income, self.parenting_desire, self.parenting)
