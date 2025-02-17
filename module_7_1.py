class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def get_products(self):
        file = open('products.txt', 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products):
        file = open('products.txt', 'a'
                                    '')
        for el in products:
            if str(el) in self.get_products():
                print(f'Продукт {str(el)} уже есть в магазине')
                file.close()
            else:
                file.write(f'{str(el)}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
