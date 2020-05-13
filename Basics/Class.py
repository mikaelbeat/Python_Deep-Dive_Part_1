
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Value must be positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Value must be positive.")
        else:
            self._heigth = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}."

    def __repr__(self):
        return f"Rectangle ({self.width}, {self.height})."

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(5, 5)
print(f"r1 area is {r1.area()}.")
print(f"r2 perimeter is {r1.perimeter()}.")
print(str(r1))
print(r1)

r2 = Rectangle(5, 10)

print(f"Is r1 equal to r2 -> {r1 == r2}.")
print(f"Is r1 area smaller than r2 -> {r1 < r2}.")

r2.width = -100