# Lab1_1
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('symbol', type=str)
parser.add_argument('first_number')
parser.add_argument('second_number')
args = parser.parse_args()
if args.first_number.isdigit() and args.second_number.isdigit():
    try:
        match args.symbol:
            case '+':
                print(int(args.first_number) + int(args.second_number))
            case '-':
                print(int(args.first_number) - int(args.second_number))
            case '*':
                print(int(args.first_number) * int(args.second_number))
            case '/':
                try:
                    print(int(args.first_number) / int(args.second_number))
                except ZeroDivisionError:
                    print('Impossible zero division')
            case _:
                print('Invalid command')
    except TypeError:
        print('Wrong arguments type')
else:
    print('Wrong argument Type')

