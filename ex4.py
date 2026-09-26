class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(3, 4)
pt_clone = pt.clone()
print("Оригинал:", pt.x, pt.y)
print("Клон:    ", pt_clone.x, pt_clone.y)