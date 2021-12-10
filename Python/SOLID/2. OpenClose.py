from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP states that a class should be open for extension but closed for modification !


class ProductFilter:
    def filterByColor(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filterBySize(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filterByuSizeAndColor(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Specification
class Specification:
    def isSatisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def isSatisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def isSatisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.isSatisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # without using OCP
    pf = ProductFilter()
    print("Green products (old)")
    for p in pf.filterByColor(products, Color.GREEN):
        print(f"- {p.name} is green")

    # with OCP!
    bf = BetterFilter()

    print("Green products (new) ")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f"- {p.name} is green")