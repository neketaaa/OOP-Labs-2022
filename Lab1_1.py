# Lab1_1
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('symbol', type=str)
parser.add_argument('first_number', type=float)
parser.add_argument('second_number', type=float)
args = parser.parse_args()
match args.symbol:
    case '+':
        print(args.first_number + args.second_number)
    case '-':
        print(args.first_number - args.second_number)
    case '*':
        print(args.first_number * args.second_number)
    case '/':
        print(args.first_number / args.second_number)
    case _:
        print('Invalid command')


