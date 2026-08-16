class Example:
    shared = 10
    def __init__(self, non_shared_):
        self.__non_shared = non_shared_
    def non_shared(self):
        return self.__non_shared

if __name__ == '__main__':
    e1, e2 = Example(20), Example(30)
    print('e1 Shared:', e1.shared)
    print('e1 Non-shared:', e1.shared())
    print('e2 Shared:', e2.shared)
    print('e2 Non-shared:', e2.shared())
    print('Change shared attribute')
    Example.shared = -10
    print('e1 Shared:', e1.shared)
    print('e1 Non-shared:', e1.shared())
    print('e2 Shared:', e2.shared)
    print('e2 Non-shared:', e2.shared())
