# Lab1_2
import argparse
import math
import operator
parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('first_number', type=float)
parser.add_argument('second_number', type=float)
args = parser.parse_args()
function = getattr(math, args.action, False)
# False is default value
if function == False:
    function = getattr(operator, args.action)
print(function(args.first_number, args.second_number))