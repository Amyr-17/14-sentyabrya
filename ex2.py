class SingletonFive:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 5:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
for o in objs:
    print(o.name, end=" ")
print()