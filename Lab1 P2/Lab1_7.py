class Product:

    def __init__(self, price_val, description_val, weight_val):
        self.price = price_val
        self.description = description_val
        self.weight = weight_val

    def show(self):
        print(f'{self.description} price: {self.price} weight: {self.weight}')



class Customer:

    def get(self):
        return self

    def __init__(self, surname_val, name_val, patronymic_val, mob_phone_val):
        self.surname = surname_val
        self.name = name_val
        self.patronymic = patronymic_val
        self.mob_phone = mob_phone_val

    def show(self):
        print(self.surname, self.name, self.patronymic, self.mob_phone)


class Order:
    customer = None
    products = []

    def __init__(self, customer_val: Customer):
        self.customer = customer_val

    def add_product(self, product: Product):
        self.products.append(product)

    def total_order(self):
        total = 0
        for i in range(len(self.products)):
            total += self.products[i].price
        return total

    def show(self):
        self.customer.show()
        for i in range(len(self.products)):
            self.products[i].show()
        print(f'Total: {self.total_order()}')


def main():
    person = Customer(input('Surname: '), input('Name: '), input('patronymic: '), input('mob_phone: '))
    print(person.get().name, person.get().surname, person.get().patronymic, person.get().mob_phone)

    example = Order(person)

    pasta = Product(1., 'Pasta', 0.5)
    example.add_product(pasta)
    pork = Product(6.5, 'Pork', 1)
    example.add_product(pork)
    tomato = Product(3.3, 'Tomato', 1)
    example.add_product(tomato)
    ketchup = Product(2.7, 'Ketchup', 0.5)
    example.add_product(ketchup)
    eggs = Product(2.2, 'Eggs', 0.6)
    example.add_product(eggs)

    print(example.show())

    # desc_val = None
    # price_val = 0.
    # weight_val = 0.
    # with open('help_for_7.txt', 'r') as file:
    #     for line in file:
    #         for word in line.split(' '):
    #             match word[0]:
    #                 case 'p': price_val = float(word)
    #                 case 'w': weight_val = float(word)
    #                 case _: desc_val += word




if __name__ == '__main__':
    main()
