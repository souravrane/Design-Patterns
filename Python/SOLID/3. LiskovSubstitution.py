class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: ${self._width}, height: ${self._height}"


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def useIt(rc):
    w = rc.width
    rc.height = 10  # violation of LSP as the inherited square class does not behave the same way as rectangle!
    expected = int(w * 10)
    print(f"Expected area {expected}, but got {rc.area}")


rc = Rectangle(2, 3)
useIt(rc)

sq = Square(5)
useIt(sq)