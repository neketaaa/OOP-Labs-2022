import argparse
import math


class Rational:
    def __init__(self, num_value=1, den_value=1):
        if isinstance(num_value, int) and isinstance(den_value, int) and den_value:
            gcd = math.gcd(num_value, den_value)
            self.numerator = num_value / gcd
            self.denominator = den_value / gcd
        else:
            raise ValueError

    def show_int(self):
        return f'{self.numerator}/{self.denominator}'

    def show_flt(self):
        return float(self.numerator) / float(self.denominator)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numerator', type=int)
    parser.add_argument('denominator', type=int)
    args = parser.parse_args()

    example = Rational(args.numerator, args.denominator)
    print(example.show_int())
    print(example.show_flt())


if __name__ == "__main__":
    main()
