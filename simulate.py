import argparse

import config
from family import Family
from person import Person
from util import PersonUtil

from numpy.random import randint


class Simulator:
    def __init__(self, start_families, start_quality, num_gens):
        self.families = []
        self.num_gens = num_gens
        self.current_gen = 0
        self.util = PersonUtil()
        self.gen_dir = 'gens/'
        self.family_counter = 1

        # Build initial families
        for _ in range(start_families):
            husband = self.util.random_person(sex=config.MALE, start=start_quality)
            wife = self.util.random_person(sex=config.FEMALE, start=start_quality)
            family = Family(husband, wife, family_line=self.family_counter)
            husband.fid = self.family_counter; wife.fid = self.family_counter
            self.families += [family]
            self.family_counter += 1

        # Add children
        self.build_children()
        self.save_gen()
        self.current_gen += 1

    def simulate(self):
        for i in range(self.num_gens):
            # Match children between families (siblings can't match)
            if len(self.families) < 2:
                return
            self.families = self.build_next_parents()

            # Generate children for each family
            self.build_children()

            # Save new generation
            self.save_gen()
            self.current_gen += 1

    def build_children(self):
        for family in self.families:
            for _ in range(self.util.num_children(family.wife, family.husband)):
                child = Person()
                child.init_self(self.util, family.wife, family.husband)
                family.add_child(child)

    def build_next_parents(self):
        dating_pool = []
        for family in self.families:
            dating_pool.extend(family.children)

        already_matched = []
        new_families = []
        print(dating_pool)
        for person in dating_pool:
            eligible = [p for p in dating_pool if p.fid != person.fid and p.sex != person.sex
                        and p.pid not in already_matched]
            print(person.name, [p.name for p in eligible])
            if len(eligible) > 0:
                e_idx = randint(len(eligible))
                partner = eligible[e_idx]
                if person.sex == config.MALE:
                    new_families += [Family(person, partner, family_line=self.family_counter)]
                else:
                    new_families += [Family(partner, person, family_line=self.family_counter)]
                already_matched.extend([person.pid, partner.pid])
                self.family_counter += 1

        return new_families

    def save_gen(self):
        save_file = '{}{}.txt'.format(self.gen_dir, self.current_gen)
        with open(save_file, 'w') as f:
            for family in self.families:
                f.write('{}\n'.format(family))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--match-method', choices=['similarity', 'quality', 'opposites', 'hybrid'])
    parser.add_argument('-n', '--start-families', type=int, default=config.NUM_FAMILIES,
                        help='initial family count')
    parser.add_argument('-q', '--start-quality', type=int, choices=[-1, 0, 1], default=config.NEUTRAL_START,
                        help='quality of initial families')
    parser.add_argument('-g', '--num-gens', type=int, default=config.NUM_GENS,
                        help='number of generations to run simulation')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    simulator = Simulator(args.start_families, args.start_quality, args.num_gens)
    simulator.simulate()
