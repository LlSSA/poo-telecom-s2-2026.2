class NetworkDevice:
    def __init__(self, name='device', address = '192.168.0.1'):
        self.__name = name
        self.__adress = address
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')
            


    def __str__(self):
        return f'NetworkDevice -> [name: {self.__name}, adress: {self.__adress}]'

class EndDevice:
    def __init__(self, name='Enddevice', address = '192.168.0.2'):
        self.__name = name
        self.__adress = address
        
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address_):
        if isinstance(address_, str) and len(address_) > 0:
            self.__address = self.address
        else:
            raise RuntimeError('EndDevice name must be a non-empty string')


def add(endDevice):
    if isinstance(endDevice, EndDevice):
        pass


def remove(self, endDevice):
    if isinstance(endDevice, EndDevice):
        pass



def __eq__(self, other):
    if isinstance(other, EndDevice):
        return self.address == other.address
    else:
        raise RuntimeError('EndDevice can only be compared to other EndDevice')


def __str__(self):
        return f'EndDevice -> [name: {self.name}, adress: {self.adress}]'





if __name__ == '__main__':
    nd1 = NetworkDevice(address='192.168.0.2')
    print(nd1)

    nd2 = NetworkDevice(nome='Switch1')
    print(nd2)


    try:
        nd3 = NetworkDevice(name='')
    except RuntimeError as e:
        print(e)

    try:
        nd4 = NetworkDevice(name=1)
    except RuntimeError as e:
        print(e)

    try:
        nd5 = NetworkDevice(address='')
    except RuntimeError as e:
        print(e)

    try:
        nd6 = NetworkDevice(address=1)
    except RuntimeError as e:
        print(e)
   

    ed = EndDevice()
    print(ed)

