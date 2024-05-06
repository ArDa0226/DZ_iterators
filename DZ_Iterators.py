
class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.step = 1


    def __iter__(self):
        self.value = self.start - self.step
        return self
    def __next__(self):
        self.start += self.step
        if self.start > 1:
            if self.start > self.end:
                raise StopIteration
        if self.start % 2 == 0:
            return self.start


en = EvenNumbers(start=10,end=25)
for i in en:
    print(i)


# for i in range(10, 25):
#     if i % 2 == 0:
#         print(i)

