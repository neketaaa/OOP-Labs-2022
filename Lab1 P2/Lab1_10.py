class BinaryTree:

    def __init__(self, data: tuple = None):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data: tuple):
        if not self.data:
            self.data = data
            return

        if data < self.data:
            if self.left:
                self.left.add(data)
                return
            self.left = BinaryTree(data)
            return

        if self.right:
            self.right.add(data)
            return
        self.right = BinaryTree(data)

    def search(self, code, quantity):
        print(self.data)
        if self.data[0] == code:
            print(float(self.data[1]) * int(quantity))
            return float(self.data[1])

        if self.data[0] > code:
            if self.left:
                self.left.search(code, quantity)
                return
            print('l')
            return 0.

        if self.right:
            self.right.search(code, quantity)
            return
        print('r')
        return 0.

def main():
    shop = BinaryTree()
    prod_list = [(323, 20.9), (154, 11.3), (248, 7.15), (874, 9.7), (560, 21.11), (239, 2.4), (647, 8.), (444, 4.14)]
    for item in range(len(prod_list)):
        shop.add(prod_list[item])

    while True:
        code = input('Enter code(''S'' to stop): ')
        if code == 'S' or code == 's':
            break
        quantity = input('Enter quantity: ')

        print(f'Price: {shop.search(int(code), quantity)}')

if __name__ == '__main__':
    main()

