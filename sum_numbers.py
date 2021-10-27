
import argparse

# Initialize parser
parser = argparse.ArgumentParser(description='Takes two values and add them')

# Adding arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for accumulator')
parser.add_argument(dest='accumulate', action='store_const', const=sum, help='sum the integers')

args = parser.parse_args()

print(args)
print(args.accumulate(args.integers))