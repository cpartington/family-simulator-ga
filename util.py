from numpy.random import randint

import config
from person import Person


# Build name lists
with open('./data/female_names.txt') as f:
    f_names = [line.strip() for line in f]
with open('./data/male_names.txt') as f:
    m_names = [line.strip() for line in f]
names = {
    config.FEMALE: f_names,
    config.MALE: m_names,
}
name_length = len(f_names)


def random_person(age: int = None, sex: int = None, start: int = config.NEUTRAL_START):
    person = Person()

    low = config.STAT_MIN
    high = config.STAT_MAX + 1
    if start == config.BAD_START:
        high = config.STAT_MAX // 2 + 1
    elif start == config.GOOD_START:
        low = config.STAT_MAX // 2

    # Basic information
    if age is None:
        age = randint(20, 30+1)
    if sex is None:
        sex = randint(0, 1+1)
    person.age = age
    person.sex = sex
    person.name = names[sex][randint(0, name_length)]

    # Personality information
    person.rebellious = randint(low, high)
    person.ambition = randint(low, high)
    person.hardworking = randint(low, high)
    person.life_goal = randint(0, 1+1)

    # Complex information
    person.education = randint(low, high)
    person.income = randint(low, high)
    person.lifestyle = randint(low, high)
    person.parenting = randint(low, high)

    return person
