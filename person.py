from config import INTERACTION_COEFFICIENT, GOAL_LUXURY

def interaction(val1, val2):
    return INTERACTION_COEFFICIENT * val1 * val2


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

        self.happiness: int = -1

    def init_self(self, util, mother, father):
        self.age = util.random_adult_age()
        self.sex = util.random_sex()
        self.name = util.random_name(self.sex)

        self.rebellious = util.random_rebellion()
        self.ambition = util.child_attribute(mother.ambition, father.ambition)
        self.hardworking = util.child_attribute(mother.hardworking, father.hardworking, self.rebellious)
        self.life_goal = util.child_life_goal(mother.life_goal, father.life_goal, self.rebellious)
        self.lifestyle = util.child_attribute(mother.lifestyle, father.lifestyle, self.rebellious)

        self.education = util.child_education(mother, father, self)
        self.income = util.child_income(self)
        self.parenting_desire = util.child_parenting_desire(mother, father, self)
        self.parenting = util.child_parenting(mother, father, self)
        self.longevity = util.child_longevity(self)

        self.get_happiness()

    def get_quality(self):
        q = self.ambition + self.hardworking + self.education + self.lifestyle + self.parenting
        return q

    def get_happiness(self):
        base = self.longevity + self.income + self.hardworking + self.lifestyle + self.education
        life_goal = self.life_goal * 50  # 0 if goal=money, 50 if goal=meaning
        nice_retirement = interaction(self.longevity, self.income)
        healthy_retirement = interaction(self.longevity, self.lifestyle)
        wealth_benefit = self.income * (1.5 if self.life_goal == GOAL_LUXURY else 1)
        self.happiness = int(0.4 * base + 0.2 * life_goal + 0.1 * nice_retirement + 0.15 * healthy_retirement
                             + 0.15 * wealth_benefit)
        # print('base: {}, life goal: {}, nice retire: {}, healthy retire: {}, wealth: {}, overall: {}'
        #       .format(base, life_goal, round(nice_retirement, 2), round(healthy_retirement, 2), wealth_benefit,
        #               self.happiness))

    def __str__(self):
        return '  {}: Age: {} Sex: {} Longevity: {}y Happiness: {}\n' \
               '    Rebellion: {} Ambition: {} Hardworking: {}\n' \
               '    Life goal: {} Lifestyle: {} Education: {}\n' \
               '    Income: {} Parenting Desire: {} Quality: {}\n'\
            .format(self.name, self.age, self.sex, self.longevity, self.happiness, self.rebellious, self.ambition,
                    self.hardworking, self.life_goal, self.lifestyle, self.education, self.income,
                    self.parenting_desire, self.parenting)
