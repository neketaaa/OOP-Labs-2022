import argparse

parser = argparse.ArgumentParser()
parser.add_argument('formula', type=str)
args = parser.parse_args()
result = True
result_value = None
i = 1
for i in range(len(args.formula) - 1):
    if not args.formula[i].isdigit():
        if args.formula[i] == '+' or args.formula[i] == '+':
            if not args.formula[i-1].isdigit():
                result = False
        else:
            result = False
if result:
    result_value = eval(args.formula)
print(f'({result}/{result_value})')
