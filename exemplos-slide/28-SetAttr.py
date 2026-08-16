class ChemistryConstants:
    __AVOGADRO = 6.02214076e23
    def __init__(self):
        pass

    @property
    def AVOGADRO(self):
        return self.__AVOGADRO
    @AVOGADRO.setter
    def AVOGADRO(self, value_):
        raise ValueError('Const can not be changed -1')
    def __setattr__(self, name_, value_):
        if name_ not in self.__dict__:
            raise ValueError('Cannot add new members to this class.')

if __name__=='__main__':
    c = ChemistryConstants()
    print(c.AVOGADRO)
    c.AVOGADRO = 20
    print(c.AVOGADRO)