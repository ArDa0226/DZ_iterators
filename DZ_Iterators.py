
class EvenNumbers:

    def __init__(self, start=0, end=1 ):
        self.start, self.end = start, end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 2
            return self.start - 2

en = EvenNumbers(10,25)
for i in en:
    print(i)


