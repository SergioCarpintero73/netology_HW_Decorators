from foo_logs import logger


# 1.
class FlatIterator:

    def __init__(self, lists: list):
        self.lists = sum(lists, [])

    def __iter__(self):
        self.cursor = - 1
        return self

    def __next__(self):
        if self.cursor == len(self.lists) - 1:
            raise StopIteration
        self.cursor += 1
        return self.lists[self.cursor]


# 2.
@logger
def flat_generator(a: list) -> list:
    return [x for target_list in a for x in target_list]

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    for item in flat_generator(nested_list):
        print(item)