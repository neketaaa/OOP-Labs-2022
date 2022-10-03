import argparse

class Rational:
    def __init__(self, num_value = 1, den_value = 1):
        self.numerator = num_value
        self.denominator = den_value

        for i in range(min(num_value, den_value), 0, -1):
            if not (int(num_value) / i) and not (int(den_value) / i):
                self.numerator = int(num_value / i)
                self.denominator = int(den_value / i)
                break

    def printer_int(self):
        print(f'{self.numerator}/{self.denominator}')

    def printer_flt(self):
        print(float(self.numerator)/float(self.denominator))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numerator', type=int)
    parser.add_argument('denominator', type=int)
    args = parser.parse_args()

    example = Rational(args.numerator, args.denominator)
    example.printer_int()
    example.printer_flt()

if __name__ == "__main__":
    main()
