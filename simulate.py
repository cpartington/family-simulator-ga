import argparse

import config
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
            print(husband)
            print(wife)
            print()

    def simulate(self):
        pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--match-method', choices=['similarity', 'quality', 'opposites'])
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
