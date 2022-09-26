class Statistic:
    file = None
    letters = 0
    words = 0
    lines = 0

    def __init__(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.lines += 1
                for word in line.split(' '):
                    self.letters += len(word)
                    print(word, len(word))
                    self.words += 1
        self.letters -= self.lines


    def show(self):
        print(f'lines: {self.lines} words: {self.words} letters: {self.letters}')

def main():
    file = Statistic(input("filename: "))
    file.show()

if __name__ == "__main__":
    main()