

import argparse
  
  
# Initializing Parser
parser = argparse.ArgumentParser(description ='sort some integers.')
  
# Adding Argument
parser.add_argument('integers',
                    metavar ='N',
                    type = float,
                    nargs ='+',
                    help ='an integer for the accumulator')
  
parser.add_argument('sum',
                    action ='store_const',
                    const = sum)
  
parser.add_argument('len',
                    action ='store_const',
                    const = len)


args = parser.parse_args()              # Instantiate parser
total_sum = args.sum(args.integers)     # Pass the numbers to "sum" argument
length = args.len(args.integers)        # Pass the numbers to "len" argument
average = total_sum / length            # Find the average
print(f"Total average is: {average}")
