import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, default=0)
parser.add_argument('-w', type=int, nargs="+", default=0)
parser.add_argument('-n', type=int, default=0)
args = parser.parse_args()
print(args.W, args.w, args.n)