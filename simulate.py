import argparse

import config
from family import Family
from person import Person
from util import PersonUtil


class Simulator:
    def __init__(self, start_families, start_quality, num_gens):
        self.families = []
        self.num_gens = num_gens
        self.util = PersonUtil()
        # Build initial families
        for _ in range(start_families):
            husband = self.util.random_person(sex=config.MALE, start=start_quality)
            wife = self.util.random_person(sex=config.FEMALE, start=start_quality)
            family = Family(husband, wife)
            self.families += [family]

        for i in range(num_gens):
            # Generate children for each family
            for family in self.families:
                for _ in range(self.util.num_children(family.wife, family.husband)):
                    child = Person()
                    child.init_self(self.util, family.wife, family.husband)
                    family.add_child(child)
                print(family)
            # Match children between families (siblings can't match)

    def simulate(self):
        pass


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
