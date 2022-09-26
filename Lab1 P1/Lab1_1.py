# Lab1_1
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('symbol', type=str)
parser.add_argument('first_number')
parser.add_argument('second_number')
args = parser.parse_args()
try:
    match args.symbol,args.first_number.isdigit(), args.second_number.isdigit():
        case '+',True,True:
            print(int(args.first_number) + int(args.second_number))
        case '-',True,True:
            print(int(args.first_number) - int(args.second_number))
        case '*',True,True:
            print(int(args.first_number) * int(args.second_number))
        case '/',True,True:
            try:
                print(int(args.first_number) / int(args.second_number))
            except ZeroDivisionError:
                print('Impossible zero division')
        case _:
            print('Invalid command or wrong type')
except TypeError:
    print('Wrong arguments type')

