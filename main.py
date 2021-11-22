nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.count = 0
        self.result = None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.result = sum(self.nested_list, [])[self.count]
        except IndexError:
            raise StopIteration
        self.count += 1
        return self.result


for item in FlatIterator(nested_list):
    print(item)


def flat_generator(nested_list):
    count = 0
    flag = True
    while flag:
        try:
            data = sum(nested_list, [])[count]
            count += 1
            yield data
        except IndexError:
            flag = False


for item in flat_generator(nested_list):
    print(item)
