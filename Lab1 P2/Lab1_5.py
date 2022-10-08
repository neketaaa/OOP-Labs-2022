class Rectangle:
    length = 1.0
    width = 1.0

    def perimetr(self):
        return self.length + self.width

    def area(self):
        return self.length * self.width

    def set(self, length_value: float, width_value: float):
        if 20. > length_value > 0.:
            self.length = length_value
        if 20. > width_value > 0.:
            self.width = width_value

    def get(self):
        return f'length: {self.length} width: {self.width}'

def main():
    example = Rectangle()
    example.set(0.03, 19.78)
    print(example.get())
    print(f'area: {example.area()}')
    print(f'perimetr: {example.perimetr()}')

if __name__=="__main__":
    main()

