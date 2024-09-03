class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start < self.end
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += 2
            if self.start % 2 == 0:
                return x
        else:
            raise StopIteration



en = EvenNumbers(10, 25)

for i in en:
    print(i)


