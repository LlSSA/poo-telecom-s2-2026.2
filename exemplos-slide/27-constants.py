class ChemistryConstants:

    __AVOGRADO = 6.02214076e23
    @staticmethod
    def AVOGRADO():
        return ChemistryConstants.__AVOGRADO

if __name__ =='__main__':
    print(ChemistryConstants.AVOGRADO())
    ChemistryConstants.AVOGRADO = 10
    print(ChemistryConstants.AVOGRADO)