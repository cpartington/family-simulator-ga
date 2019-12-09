from numpy.random import randint

import config
from person import Person


class PersonUtil:
    def __init__(self):
        with open('./data/female_names.txt') as f:
            f_names = [line.strip() for line in f]
        with open('./data/male_names.txt') as f:
            m_names = [line.strip() for line in f]

        self.names = {
            config.FEMALE: f_names,
            config.MALE: m_names,
        }
        self.num_names = len(f_names)

    def random_person(self, age: int = None, sex: int = None, start: int = config.NEUTRAL_START):
        person = Person()

        low = config.STAT_MIN
        high = config.STAT_MAX + 1
        if start == config.BAD_START:
            high = config.STAT_MAX // 2 + 1
        elif start == config.GOOD_START:
            low = config.STAT_MAX // 2

        # Basic information
        if age is None:
            age = self.random_adult_age()
        if sex is None:
            sex = self.random_sex()
        person.age = age
        person.sex = sex
        person.name = self.random_name(sex)

        # First order information
        person.rebellious = randint(low, high)
        person.ambition = randint(low, high)
        person.hardworking = randint(low, high)
        person.life_goal = randint(0, 2)
        person.lifestyle = randint(low, high)

        # Second order information
        person.education = randint(low, high)
        person.income = randint(low, high)
        person.parenting_desire = randint(low, high)
        person.parenting = randint(low, high)
        person.longevity = self.child_longevity(person)

        person.get_happiness()

        return person

    def random_adult_age(self):
        return randint(20, 26)

    def random_sex(self):
        return randint(config.FEMALE, config.MALE + 1)

    def random_rebellion(self):
        # random number between [-STAT_MAX, +STAT_MAX]
        return randint(config.STAT_MIN, config.STAT_MAX * 2 + 1) - config.STAT_MAX

    def random_name(self, sex):
        return self.names[sex][randint(0, self.num_names)]

    def child_attribute(self, p1, p2, r=None):
        avg = (p1 + p2) / 2
        if r is None:
            jitter = randint(0, config.JITTER * 2 - 1) - config.JITTER
        else:
            jitter = r * 0.5
        subfinal = int(avg + jitter)
        return min(max(subfinal, config.STAT_MIN), config.STAT_MAX)

    def child_life_goal(self, p1, p2, r):
        if p1 != p2:
            return randint(0, 2)
        if abs(r) > config.STAT_MAX * 3/4:
            return (p1 + 1) % 2
        else:
            return p1

    def child_education(self, mother, father, child):
        p_education = (mother.education + father.education) / 2
        p_income = (mother.income + father.income) / 2
        return int(p_education * 0.25 + p_income * 0.25 + child.hardworking * 0.5)

    def child_income(self, child):
        return int(child.ambition * 0.1 + child.education * 0.65 + child.hardworking * 0.25)

    def child_parenting_desire(self, mother, father, child):
        p_parenting = (mother.parenting + father.parenting) / 2
        life_goal_effect = config.STAT_MID if child.life_goal == config.GOAL_MEANING else -config.STAT_MID
        subfinal = int(p_parenting * 0.3 + child.income * 0.3 + life_goal_effect)
        return min(max(subfinal, config.STAT_MIN), config.STAT_MAX)

    def child_parenting(self, mother, father, child):
        p_parenting = (mother.parenting + father.parenting) / 2
        return int(p_parenting * 0.3 + child.parenting_desire * 0.4 + child.hardworking * 0.3)

    def child_longevity(self, child):
        # lifestyle, income
        stat = child.lifestyle * 0.5 + child.income * 0.5
        age1 = int(stat / (stat + 15) * config.MAX_AGE)  # for average stats
        age2 = int(stat / config.STAT_MAX * config.MAX_AGE)  # for worse stats
        return max(age1, age2, 65)

    def num_children(self, mother, father):
        p_desire = (mother.parenting_desire + father.parenting_desire) / 2
        return int(p_desire / 100 * 5)
