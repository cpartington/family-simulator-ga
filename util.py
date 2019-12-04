from numpy.random import randint

import config
from config import STAT_MIN, STAT_MAX
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


def random_person(age: int = None, sex: int = None):
    person = Person()

    # Basic information
    if age is None:
        age = randint(20, 30+1)
    if sex is None:
        sex = randint(0, 1+1)
    person.age = age
    person.sex = sex
    person.name = names[sex][randint(0, name_length)]

    # Personality information
    person.rebellious = randint(STAT_MIN, STAT_MAX+1)
    person.ambition = randint(STAT_MIN, STAT_MAX+1)
    person.hardworking = randint(STAT_MIN, STAT_MAX+1)
    person.life_goal = randint(0, 1+1)

    # Complex information
    person.education = randint(STAT_MIN, STAT_MAX+1)
    person.income = randint(STAT_MIN, STAT_MAX+1)
    person.lifestyle = randint(STAT_MIN, STAT_MAX+1)
    person.parenting = randint(STAT_MIN, STAT_MAX+1)

    return person
