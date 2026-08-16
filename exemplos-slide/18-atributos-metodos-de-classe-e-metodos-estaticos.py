class CountObj:
    __quantity = 0
    def __init__(self, data_):
        self.__data = data_
        CountObj.__quantity = CountObj.__quantity + 1

    @classmethod
    def reset_counter(cls):
        cls.__quantity = 0

    @staticmethod
    def get_num_obj():
        return CountObj.__quantity

if  __name__ == "__main__":
    obj1, obj2 = CountObj(-10), CountObj(20)
    print('# of instances since last reset:', CountObj.get_num_obj())
    CountObj.reset_counter()
    print('# of instances since last reset: ', CountObj.get_num_obj())