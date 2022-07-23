import math


class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    def __add__(self, other):
        new_words = self.words + " AND " + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page("Tim is a great instructor", 1)
page2 = Page("Tim is a another page", 2)

page3 = page1 + page2
print(page3.words, page3.page_number)


class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.after_tax_price = 0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.TAX), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)


bread = StoreItem("Bread", 7)
discounted_bread = bread * 0.8
print(discounted_bread.after_tax_price)


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __truediv__(self, factor):
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

    def __floordiv__(self, factor):
        new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)


line1 = Line((10, 5), (20, 10))
line2 = line1 / 2
print(line2.point1, line2.point2)

line1 = Line((10, 5), (20, 10))
line2 = line1 // 2
print(line2.point1, line2.point2)

print(len(line1))
