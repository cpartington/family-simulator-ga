import argparse
import config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='initial family count (default is 5)')
    parser.add_argument('-q', type=int, choices=[-1, 0, 1], help='quality of initial families (default is neutral')
    args = parser.parse_args()
    return args


def simulate():
    pass


if __name__ == '__main__':
    args = parse_args()

    num_families = args.n if args.n is not None else config.NUM_FAMILIES
    start_quality = args.q if args.q is not None else config.NEUTRAL_START

    simulate()
